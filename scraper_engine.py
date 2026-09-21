import requests
from bs4 import BeautifulSoup
import re
import time
import random


class WikiTaxonomyError(Exception):
    pass


session = requests.Session()


def clean_text_fully(text):
    # Remove the dagger symbol, citations, and parentheses
    text = text.replace('†', '')
    text = re.sub(r'\[.*?\]', '', text)
    text = re.sub(r'\(.*?\)', '', text)
    return text.replace(',', '').split()


def clean_value(rank, text):
    words = clean_text_fully(text)
    if not words: return ""

    # Species Exception: Keep first two words
    if "species" in rank.lower():
        return " ".join(words[:2])

    # General Rule: If 2nd word is Capitalized (Author), take only 1st
    if len(words) > 1 and words[1][0].isupper():
        return words[0]

    return words[0]


def get_full_taxonomy(organism_name):
    formatted_name = organism_name.strip().replace(' ', '_')
    url = f"https://en.wikipedia.org/wiki/{formatted_name}"

    headers = {
        'User-Agent': 'MyTaxonomyBot/1.0 (Contact: your-email@example.com) Chrome/120.0.0.0',
    }

    try:
        response = session.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
    except Exception as e:
        raise WikiTaxonomyError(f"Connection failed: {e}")

    infobox = soup.find("table", class_=lambda x: x and ('biota' in x or 'infobox' in x))
    if not infobox:
        raise WikiTaxonomyError("No Infobox found.")

    taxonomy_results = []

    core_ranks = [
        "domain", "kingdom", "phylum", "class", "order", "family", "genus", "species",
        "clade", "division", "sub", "stem", "crown", "super", "infra", "series", "group"
    ]

    for row in infobox.find_all("tr"):
        cells = row.find_all(['th', 'td'])
        if len(cells) >= 2:

            raw_rank = cells[0].get_text().strip().replace(":", "").replace('†', '')

            
            if any(k in raw_rank.lower() for k in core_ranks):
                value_raw = cells[1].get_text(separator=" ").strip()


                final_value = clean_value(raw_rank, value_raw)
                final_value = final_value.replace(" (unranked)", "").split("Edit")[0].strip()

                if raw_rank and final_value:
                    if "binomial" in raw_rank.lower():
                        break

                    # Clean "Extinct" from the rank display
                    display_rank = raw_rank.replace("Extinct ", "").strip()
                    taxonomy_results.append((display_rank, final_value))

    return taxonomy_results


def run_app(sink):
    print("--- Organism Taxonomy Scraper ---")
    print("Commands: 'q' to quit")

    while True:
        user_input = input("\nEnter organism name: ")
        if user_input.lower() == 'q':
            break

        try:
            taxonomy = get_full_taxonomy(user_input)
            sink(user_input, taxonomy)

            # THE BYPASS: Randomly wait 1 to 3 seconds between searches.
            # This makes the traffic look "human" and prevents 429 errors.
            print("\n(Waiting a moment to respect Wikipedia's limits...)")
            time.sleep(random.uniform(1.5, 3.5))

        except WikiTaxonomyError as e:
            print(f"\n[ERROR] {e}")
        except Exception as e:
            print(f"\n[UNEXPECTED ERROR] {e}")