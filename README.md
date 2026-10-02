# Live

[![MkDocs](https://img.shields.io/badge/MkDocs-1.6-526CFE?logo=materialformkdocs&logoColor=white)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/theme-Material-526CFE?logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![uv](https://img.shields.io/badge/uv-managed-DE5FE9?logo=uv&logoColor=white)](https://docs.astral.sh/uv/)
[![Docs](https://github.com/CaseyJohnson-RS/Live/actions/workflows/docs.yml/badge.svg)](https://caseyjohnson-rs.github.io/Live/)

Сайт **Live** — компьютерной игры по мотивам русской рулетки.

## Описание

Здесь живёт сайт игры: главная страница, полный свод правил в разделе
«Об игре» и блог о том, как движется проект. Сайт собирается на
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) и
публикуется на GitHub Pages при каждом пуше в `main`.

Сайт: <https://caseyjohnson-rs.github.io/Live/>

## Проект

| Репозиторий | Что внутри |
| --- | --- |
| **Live** | Сайт игры: правила и блог (этот репозиторий) |
| [LiveEngine](https://github.com/CaseyJohnson-RS/LiveEngine) | Сервер, который ведёт игру |
| Клиент | Приложение, за которым будет сидеть игрок (в планах) |

## Что где лежит

```text
docs/
├── index.md                главная: кинескоп, проект, корни
├── about/                  «Об игре»: обзор, правила, каталог, глоссарий
├── blog/                   хронология проекта
├── assets/                 фишки, обложки референсов, карта изгиба экрана
└── stylesheets/            тема «Бутылочное стекло»: палитра, общее,
                            карточки, главная, блог, правила
tools/
└── table_chips.py          генератор фишек на столе вокруг кинескопа
mkdocs.yml                  настройки сайта и навигация
```

## Локальный запуск

```bash
uv sync
uv run mkdocs serve
```

Сайт откроется на <http://127.0.0.1:8000/>.

Фишки вокруг кинескопа на главной нарисованы генератором. Другой расклад
или плотность — параметры в начале `tools/table_chips.py`, затем:

```bash
uv run python tools/table_chips.py
```

---

© 2026 Casey Johnson. Все права защищены.
