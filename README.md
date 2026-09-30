# Live

[![MkDocs](https://img.shields.io/badge/MkDocs-1.6-526CFE?logo=materialformkdocs&logoColor=white)](https://www.mkdocs.org/)
[![Material for MkDocs](https://img.shields.io/badge/theme-Material-526CFE?logo=materialformkdocs&logoColor=white)](https://squidfunk.github.io/mkdocs-material/)
[![uv](https://img.shields.io/badge/uv-managed-DE5FE9?logo=uv&logoColor=white)](https://docs.astral.sh/uv/)
[![Docs](https://github.com/CaseyJohnson-RS/Live/actions/workflows/docs.yml/badge.svg)](https://caseyjohnson-rs.github.io/Live/)

Правила **Live** — настольной игры по мотивам русской рулетки.

## Описание

Здесь живёт сайт с правилами игры: сами правила, предметы, глоссарий и
блог о том, как движется проект. Сайт собирается на
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/) и
публикуется на GitHub Pages при каждом пуше в `main`.

Сайт: <https://caseyjohnson-rs.github.io/Live/>

## Проект

| Репозиторий | Что внутри |
| --- | --- |
| **Live** | Правила игры (этот репозиторий) |
| [LiveEngine](https://github.com/CaseyJohnson-RS/LiveEngine) | Сервер, который ведёт партию |
| Клиент | Приложение, за которым будет сидеть игрок (в планах) |

## Локальный запуск

```bash
uv sync
uv run mkdocs serve
```

Сайт откроется на <http://127.0.0.1:8000/>.

---
