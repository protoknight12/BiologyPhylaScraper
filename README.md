# BiologyPhylaScraper
A python scraper built to extract different organisms' phyla into .md files(Recommended to use with Obsidian)

## Setup
```
pip install -r requirements.txt
```

## Files
- `scraper_engine.py` — scrapes an organism's Wikipedia infobox for taxonomy ranks (`get_full_taxonomy`), runs the interactive prompt loop (`run_app`), and runs a fixed-list batch fetch with a cooldown (`run_batch`)
- `main_Terminal.py` — prints results to the terminal
- `main_File.py` — writes results as `.md` files (edit the hardcoded output path for your setup)
- `fetch_200_animals.py` / `fetch_200_plants.py` / `fetch_200_fungi.py` — example bulk-fetch scripts: scrape a fixed list of 200 well-known species per kingdom instead of prompting interactively
- `fetch_protists.py` — same idea for Protista, but ~70 species: there aren't 200 protists a non-specialist would recognize
