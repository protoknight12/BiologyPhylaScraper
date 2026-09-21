from scraper_engine import run_batch
from main_File import file_sink

# Example bulk-fetch script: scrapes a fixed list instead of prompting interactively.
PLANTS = [
    # Trees
    "Pedunculate oak", "White oak", "Red maple", "Sugar maple", "Silver birch",
    "Weeping willow", "European beech", "American beech", "Giant sequoia", "Coast redwood",
    "Douglas fir", "Norway spruce", "Scots pine", "Eastern white pine", "Ginkgo biloba",
    "Monkey puzzle tree", "Common fig", "Olive", "Japanese cherry", "Southern magnolia",
    "Flowering dogwood", "Eucalyptus globulus", "Rainbow eucalyptus", "Coconut palm",
    "Date palm", "Banana", "Mango", "Avocado", "Apple", "European pear", "Peach", "Lemon",
    "Sweet orange", "Cacao tree", "Coffea arabica", "Camellia sinensis", "Para rubber tree",
    "Teak", "Big-leaf mahogany", "Bamboo", "Giant timber bamboo", "Weeping fig", "Banyan",
    "African baobab", "Joshua tree", "Saguaro", "Great Basin bristlecone pine",
    "European horse chestnut", "Common hazel", "European ash",
    # Flowers
    "Rose", "Tulip", "Common sunflower", "Common daisy", "Easter lily", "Moth orchid",
    "Daffodil", "Carnation", "Peony", "Iris", "Common poppy", "Marigold", "Chrysanthemum",
    "Hydrangea", "Lavender", "Hibiscus", "Sacred lotus", "White water lily",
    "Common dandelion", "Sweet violet", "Garden pansy", "Petunia", "Begonia", "Jasmine",
    "Gardenia", "Camellia japonica", "Azalea", "Rhododendron", "Strelitzia reginae",
    "Amaryllis", "Snapdragon", "Zinnia", "Cosmos", "Freesia", "Anemone", "Crocus",
    "Common bluebell", "Common foxglove", "Hyacinth", "Forget-me-not",
    # Succulents & cacti
    "Aloe vera", "Prickly pear", "Jade plant", "Echeveria elegans", "Golden barrel cactus",
    "Christmas cactus", "Agave americana", "Snake plant", "Lithops", "Zebra plant",
    # Grasses & crops
    "Common wheat", "Rice", "Maize", "Barley", "Oat", "Sugarcane", "Sorghum", "Rye",
    "Common reed", "Pampas grass",
    # Vegetables
    "Tomato", "Potato", "Carrot", "Onion", "Garlic", "Cucumber", "Cabbage", "Lettuce",
    "Spinach", "Broccoli", "Cauliflower", "Pumpkin", "Zucchini", "Bell pepper",
    "Chili pepper", "Eggplant", "Radish", "Beetroot", "Celery", "Asparagus", "Green bean",
    "Pea", "Sweet potato", "Turnip", "Leek",
    # Fruits
    "Garden strawberry", "Blueberry", "Raspberry", "Blackberry", "Common grape vine",
    "Watermelon", "Cantaloupe", "Pineapple", "Papaya", "Kiwifruit", "Pomegranate",
    "Passionfruit", "Guava", "Lychee", "Durian", "Jackfruit", "Cherry", "Plum", "Apricot",
    "Persimmon", "Star fruit", "Dragon fruit", "Mangosteen", "Rambutan", "Fig",
    # Herbs & other
    "Basil", "Mentha", "Rosemary", "Thyme", "Oregano", "Common sage", "Parsley",
    "Coriander", "Dill", "Chamomile", "Venus flytrap", "Pitcher plant", "Sundew",
    "Stinging nettle", "Poison ivy", "European mistletoe", "Common ivy", "Bracken",
    "Maidenhair fern", "Sphagnum", "Field horsetail", "White clover", "Alfalfa",
    "Water hyacinth", "Common duckweed", "Bulrush", "Papyrus sedge", "Common milkweed",
    "Poinsettia", "Balsam fir", "Holly", "Wisteria", "Bougainvillea", "Morning glory",
    "Honeysuckle", "Clematis", "Common lilac", "Forsythia", "European yew", "Common juniper",
]

assert len(PLANTS) == 200, f"expected 200 plants, got {len(PLANTS)}"

if __name__ == "__main__":
    run_batch(PLANTS, file_sink, cooldown=2)
