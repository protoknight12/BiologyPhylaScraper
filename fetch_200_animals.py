import time

from scraper_engine import get_full_taxonomy, WikiTaxonomyError
from main_File import file_sink

# Example bulk-fetch script: scrapes a fixed list instead of prompting interactively.
ANIMALS = [
    # Mammals
    "Lion", "Tiger", "Leopard", "Cheetah", "Jaguar", "African elephant", "Asian elephant",
    "Giraffe", "Zebra", "Hippopotamus", "White rhinoceros", "Black rhinoceros", "Gorilla",
    "Chimpanzee", "Orangutan", "Bonobo", "Kangaroo", "Koala", "Wombat", "Platypus",
    "Red fox", "Arctic fox", "Gray wolf", "Coyote", "Brown bear", "Polar bear",
    "American black bear", "Giant panda", "Red panda", "Raccoon", "Striped skunk",
    "Eurasian otter", "Sea otter", "Beaver", "Red squirrel", "Hedgehog", "Vampire bat",
    "Bottlenose dolphin", "Orca", "Blue whale", "Humpback whale", "Sperm whale", "Narwhal",
    "Walrus", "Harbor seal", "California sea lion", "Manatee", "Dromedary", "Llama",
    "Alpaca", "Horse", "Domestic donkey", "Domestic pig", "Domestic sheep", "Domestic goat",
    "Red deer", "Moose", "Reindeer", "American bison", "African buffalo", "Blue wildebeest",
    "Thomson's gazelle", "Impala", "Common warthog", "Spotted hyena", "Meerkat",
    "Nine-banded armadillo", "Giant anteater", "Aardvark", "European hare",
    # Birds
    "Bald eagle", "Golden eagle", "Peregrine falcon", "Great horned owl", "Snowy owl",
    "Barn owl", "Common ostrich", "Emu", "Emperor penguin", "King penguin", "Flamingo",
    "Mallard", "Mute swan", "Canada goose", "Wild turkey", "Common raven", "American crow",
    "Blue jay", "Northern cardinal", "European robin", "House sparrow", "Barn swallow",
    "Ruby-throated hummingbird", "Toucan", "Scarlet macaw", "African grey parrot",
    "Budgerigar", "Common kingfisher", "Great blue heron", "Secretarybird",
    "Rüppell's vulture", "Andean condor", "Common pheasant", "Rock dove", "House finch",
    "Atlantic puffin", "Common kiwi", "Cassowary", "Wandering albatross", "Shoebill",
    # Reptiles
    "Komodo dragon", "Green iguana", "Veiled chameleon", "Panther chameleon",
    "Bearded dragon", "Nile crocodile", "American alligator", "Saltwater crocodile",
    "Galápagos tortoise", "Green sea turtle", "Leatherback sea turtle", "King cobra",
    "Indian cobra", "Black mamba", "Ball python", "Reticulated python", "Boa constrictor",
    "Gila monster", "Common snapping turtle", "Eastern box turtle", "Tokay gecko",
    "Leopard gecko", "Green anole", "Monitor lizard", "Diamondback rattlesnake",
    # Amphibians
    "American bullfrog", "Poison dart frog", "Red-eyed tree frog", "Axolotl",
    "Fire salamander", "Cane toad", "Common toad", "Tiger salamander", "Goliath frog",
    "Hellbender",
    # Fish
    "Great white shark", "Whale shark", "Great hammerhead", "Tiger shark", "Gray reef shark",
    "Clownfish", "Blue tang", "Koi", "Goldfish", "Atlantic salmon", "Rainbow trout",
    "Piranha", "Electric eel", "Giant manta ray", "Stingray", "Seahorse", "Angelfish",
    "Siamese fighting fish", "Swordfish", "Atlantic bluefin tuna",
    # Invertebrates & insects
    "Monarch butterfly", "Western honey bee", "Bumblebee", "Coccinellidae", "Praying mantis",
    "Dragonfly", "Firefly", "Common fruit fly", "Housefly", "Ant", "Fire ant", "Termite",
    "Tarantula", "Black widow spider", "Scorpion", "Emperor scorpion",
    "Giant Pacific octopus", "Common cuttlefish", "Humboldt squid", "Giant squid",
    "Colossal squid", "Blue-ringed octopus", "Moon jellyfish", "Box jellyfish",
    "Portuguese man o' war", "Giant clam", "Garden snail", "Banana slug", "Earthworm",
    "American lobster", "Blue crab", "Coconut crab", "Horseshoe crab", "Mantis shrimp",
    "Hermit crab",
]

assert len(ANIMALS) == 200, f"expected 200 animals, got {len(ANIMALS)}"

if __name__ == "__main__":
    for i, name in enumerate(ANIMALS, 1):
        try:
            resolved_name, taxonomy, image_url = get_full_taxonomy(name)
            file_sink(name, taxonomy, image_url)
            print(f"[{i}/200] OK: {name} ({len(taxonomy)} ranks, image={bool(image_url)})")
        except WikiTaxonomyError as e:
            print(f"[{i}/200] FAIL: {name}: {e}")
        time.sleep(5)
