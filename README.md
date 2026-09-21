# BiologyPhylaScraper
A python scraper built to extract different organisms' phyla into .md files(Recommended to use with Obsidian)

## Setup
```
pip install -r requirements.txt
```

## Files
- `scraper_engine.py` — scrapes an organism's Wikipedia infobox for taxonomy ranks (`get_full_taxonomy`) and runs the interactive prompt loop (`run_app`)
- `main_Terminal.py` — prints results to the terminal
- `main_File.py` — writes results as `.md` files (edit the hardcoded output path for your setup)
