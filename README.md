# Data Practice Atlas

A curated, filterable index of books, people, studios, festivals, data portals, dataset sources, weird datasets, websites, videos and tools at the meeting point of data, design, journalism and rights.

**Browse it:** open the GitHub Pages site for this repository.

## Licence

Data and written content: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See `LICENSE`. The Tool category credits Andy Kirk's Visualising Data catalogue.

## What's here

| Path | What it is |
|---|---|
| `index.html` | The explorable page: search, filter by category, Tool section, theme, status and link check; sort; card or table view. |
| `data/atlas.json` | All records, one object per entry. The page loads this file. |
| `data/atlas.csv` | The same records as CSV (tags separated by `;`). |
| `scripts/` | The Python that builds the data files, plus the raw Visualising Data catalogue extract. |

## Fields

`id`, `name`, `category`, `who`, `year`, `place`, `tags`, `note`, `url`, `seed` (true = in the original personal list), `status` (active / archived / historical / unclear), `verified`.

## Data governance and constraints

**Provenance.** Seeded from a personal list and expanded with Claude on 19 Nov 2026. The Tool category reproduces Andy Kirk's [Visualising Data resources catalogue](https://visualisingdata.com/resources/) (293 tools, read 19 Nov 2026) in its seven original sections, without descriptions.

**Verification.** The `verified` field says which of three states each record is in:
- `verified this session`: checked against a live source on 19 Nov 2026.
- `from Claude's knowledge; check link`: added from general knowledge, with a direct link that has not been checked.
- `no link confirmed; search link`: no reliable link found; the URL is a web search.

**Corrections.** About a dozen links on the Visualising Data catalogue page are attached to the wrong tile (e.g. Vega and Vega-Lite, Plotly and Dash). This dataset corrects them and notes it on each record.

**Gaps.** Leans towards Europe, North America and English-language work despite deliberate additions from Latin America, Africa, MENA, South and Southeast Asia and Italy. Years and places are blank where not confirmed. Event dates change.

**Permitted use.** A starting reading, contacts and tools list for teaching, inspiration and programme research.

**Not for.** Citation without checking each link; claims that the list is complete or representative; ranking people or studios.

## Rebuilding the data

```bash
cd scripts
python3 build_data.py      # writes data.json and data.csv here
mv data.json ../data/atlas.json && mv data.csv ../data/atlas.csv
```

To add an entry, append a tuple to `scripts/additions.py` in the same field order and rebuild.
