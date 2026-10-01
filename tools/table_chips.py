"""Фишки на столе вокруг кинескопа главной страницы.

Рисует два слоя: docs/assets/table-back.svg (за кинескопом) и
docs/assets/table-front.svg (перед ним). Оба в одной системе координат:
кинескоп занимает x 320–1200, его нижний край — y 480; чем выше фишка
(меньше y), тем она дальше: меньше, площе, бледнее и размытее.

Запуск: uv run python tools/table_chips.py
"""

import random
from pathlib import Path

W, H = 1520, 600          # рамка слоя; CSS растягивает её по ширине кинескопа
CRT_LEFT, CRT_RIGHT, CRT_BOTTOM = 320, 1200, 480
NEAR_Y, FAR_Y = 590, 250  # ближний и дальний край стола
SEED = 7                  # другой расклад — другое число

OUT = Path(__file__).resolve().parent.parent / "docs" / "assets"


def lerp(a: float, b: float, t: float) -> float:
    return a + (b - a) * t


def depth(y: float) -> float:
    """0 — у самого края стола, 1 — в глубине зала."""
    return min(1.0, max(0.0, (NEAR_Y - y) / (NEAR_Y - FAR_Y)))


def blur_level(y: float) -> int:
    """Глубина резкости: в фокусе — плоскость кинескопа."""
    if y < CRT_BOTTOM:
        return round((CRT_BOTTOM - y) / (CRT_BOTTOM - FAR_Y) * 5)
    return round(max(0.0, y - 530) / 60 * 2)


def chip(cx: float, cy: float, s: float, flat: float) -> str:
    rx, ry, h = 44 * s, 14 * s * flat, 9 * s
    stripes = "".join(
        f'<rect x="{cx + dx * s - 3 * s:.1f}" y="{cy:.1f}" width="{6 * s:.1f}" '
        f'height="{h:.1f}" fill="#c3ccd4"/>'
        for dx in (-34, -12, 12, 34)
    )
    return (
        f'<ellipse cx="{cx:.1f}" cy="{cy + h:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="#0a1c1c"/>'
        f'<rect x="{cx - rx:.1f}" y="{cy:.1f}" width="{2 * rx:.1f}" height="{h:.1f}" fill="#0a1c1c"/>'
        + stripes
        + f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx:.1f}" ry="{ry:.1f}" fill="#10292a" stroke="#1b3b3c"/>'
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx - 6 * s:.1f}" ry="{max(ry - 2 * s, 1):.1f}" '
        f'fill="none" stroke="#c3ccd4" stroke-width="{5 * s:.1f}" stroke-dasharray="{16 * s:.1f} {15 * s:.1f}"/>'
        f'<ellipse cx="{cx:.1f}" cy="{cy:.1f}" rx="{rx - 18 * s:.1f}" ry="{max(ry - 6 * s * flat, 1):.1f}" '
        f'fill="#0a1c1c" stroke="#3ee8ff" stroke-width="{1.5 * s:.1f}"/>'
    )


def pile(x: float, y: float, rng: random.Random) -> tuple[float, str]:
    """Стопка из 1–5 фишек; возвращает глубину для сортировки и разметку."""
    d = depth(y)
    s = lerp(1.15, 0.38, d)
    flat = lerp(1.0, 0.7, d)
    count = rng.choices([1, 1, 2, 3, 4, 5], k=1)[0]
    parts = []
    for i in range(count):
        jitter = rng.uniform(-3, 3) * s
        parts.append(chip(x + jitter, y - i * 9 * s, s, flat))
    opacity = lerp(1.0, 0.28, d)
    blur = blur_level(y)
    filt = f' filter="url(#b{blur})"' if blur else ""
    return y, f'<g opacity="{opacity:.2f}"{filt}>{"".join(parts)}</g>'


def scatter(rng: random.Random, n: int, xs, ys) -> list[tuple[float, str]]:
    return [pile(rng.uniform(*rng.choice(xs)), rng.uniform(*ys), rng) for _ in range(n)]


def svg(piles: list[tuple[float, str]], note: str) -> str:
    filters = "".join(
        f'<filter id="b{i}" x="-20%" y="-50%" width="140%" height="200%">'
        f'<feGaussianBlur stdDeviation="{i * 0.7:.1f}"/></filter>'
        for i in range(1, 6)
    )
    body = "\n  ".join(markup for _, markup in sorted(piles))
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">\n'
        f"  <!-- {note}. Сгенерировано tools/table_chips.py -->\n"
        f"  <defs>{filters}</defs>\n  {body}\n</svg>\n"
    )


def main() -> None:
    rng = random.Random(SEED)
    sides = [(40, CRT_LEFT + 60), (CRT_RIGHT - 60, W - 40)]
    everywhere = [(40, W - 40)]
    # за кинескопом: от глубины зала до его подножия, по бокам и в просветах
    back = scatter(rng, 26, sides, (FAR_Y, CRT_BOTTOM - 10))
    back += scatter(rng, 8, everywhere, (FAR_Y, CRT_BOTTOM - 120))
    # перед кинескопом: ближний край стола, не заслоняя экран
    front = scatter(rng, 10, sides, (CRT_BOTTOM + 10, NEAR_Y))
    front += scatter(rng, 3, [(CRT_LEFT + 80, CRT_RIGHT - 80)], (CRT_BOTTOM + 60, NEAR_Y))
    (OUT / "table-back.svg").write_text(svg(back, "Фишки за кинескопом"), encoding="utf-8")
    (OUT / "table-front.svg").write_text(svg(front, "Фишки перед кинескопом"), encoding="utf-8")


if __name__ == "__main__":
    main()
