from scraper_engine import run_batch
from main_File import file_sink

# Example bulk-fetch script: scrapes a fixed list instead of prompting interactively.
FUNGI = [
    # Edible mushrooms
    "Agaricus bisporus", "Portobello mushroom", "Shiitake", "Oyster mushroom",
    "Enokitake", "Chanterelle", "Morchella", "Porcini", "Truffle", "Black truffle",
    "Ganoderma lucidum", "Lion's mane mushroom", "Maitake", "King trumpet mushroom",
    "Auricularia auricula-judae", "Puffball", "Calvatia gigantea", "Armillaria mellea",
    "Macrolepiota procera", "Field mushroom", "Chicken of the woods", "Beefsteak fungus",
    "Cauliflower fungus", "Black chanterelle", "Summer truffle", "Matsutake",
    "Milk-cap", "Saffron milk cap", "Parasol mushroom", "Shaggy ink cap",
    # Toxic / notable
    "Death cap", "Destroying angel", "Fly agaric", "Panther cap", "Deadly webcap",
    "False morel", "Jack-o'-lantern mushroom", "Conocybe filaris", "Galerina marginata",
    "Amanita muscaria", "Amanita pantherina", "Gyromitra esculenta",
    "Psilocybe cubensis", "Psilocybe semilanceata",
    # Molds
    "Penicillium", "Penicillium chrysogenum", "Aspergillus", "Aspergillus niger",
    "Aspergillus flavus", "Aspergillus fumigatus", "Rhizopus", "Rhizopus stolonifer",
    "Mucor", "Trichoderma", "Fusarium", "Stachybotrys chartarum", "Alternaria",
    "Cladosporium", "Botrytis cinerea",
    # Yeasts
    "Saccharomyces cerevisiae", "Candida albicans", "Candida auris",
    "Schizosaccharomyces pombe", "Cryptococcus neoformans",
    # Plant pathogens
    "Ophiostoma ulmi", "Cryphonectria parasitica", "Puccinia graminis", "Ustilago maydis",
    "Claviceps purpurea", "Erysiphe", "Magnaporthe oryzae", "Fusarium oxysporum",
    "Verticillium dahliae", "Botrytis", "Venturia inaequalis", "Rhizoctonia solani",
    # Human/animal pathogens
    "Histoplasma capsulatum", "Pneumocystis jirovecii", "Trichophyton rubrum",
    "Epidermophyton floccosum", "Malassezia", "Blastomyces dermatitidis",
    "Coccidioides immitis", "Sporothrix schenckii", "Batrachochytrium dendrobatidis",
    "Microsporum canis",
    # Shelf/polypore fungi
    "Turkey tail", "Birch polypore", "Fomes fomentarius", "Ganoderma applanatum",
    "Laetiporus sulphureus", "Polyporus squamosus", "Trametes versicolor",
    # Lichens (fungal partner)
    "Lichen", "Cladonia rangiferina", "Usnea", "Xanthoria parietina",
    # Entomopathogenic / parasitic
    "Cordyceps", "Cordyceps militaris", "Ophiocordyceps unilateralis", "Cordyceps sinensis",
    # Other notable species
    "Rhizopus oryzae", "Neurospora crassa", "Aspergillus oryzae", "Trichophyton mentagrophytes",
    "Ceratocystis", "Geastrum", "Phallus impudicus", "Clathrus ruber", "Morchella esculenta",
    "Boletus edulis", "Cantharellus cibarius", "Russula emetica", "Lactarius deliciosus",
    "Coprinus comatus", "Hydnum repandum", "Sparassis crispa", "Pleurotus eryngii",
    "Flammulina velutipes", "Hericium erinaceus", "Grifola frondosa", "Tremella fuciformis",
    "Xylaria polymorpha", "Daldinia concentrica", "Hypholoma fasciculare",
    "Panaeolus", "Inocybe", "Cortinarius", "Boletus edulis var. reticulatus",
    "Suillus luteus", "Leccinum scabrum", "Craterellus cornucopioides",
    "Morchella conica", "Verpa bohemica", "Gyroporus cyanescens",
    "Hygrocybe coccinea", "Marasmius oreades", "Pluteus cervinus",
    "Lepista nuda", "Tricholoma matsutake", "Tricholoma equestre",
    "Clitocybe nuda", "Paxillus involutus", "Scleroderma citrinum",
    "Entoloma sinuatum", "Pholiota squarrosa", "Kuehneromyces mutabilis",
    "Agrocybe praecox", "Bjerkandera adusta", "Schizophyllum commune",
    "Auricularia polytricha", "Calocera viscosa", "Tremella mesenterica",
    "Exidia glandulosa", "Stereum hirsutum", "Piptoporus betulinus",
    "Inonotus obliquus", "Fomitopsis pinicola", "Ganoderma tsugae",
    "Phellinus igniarius", "Trametes hirsuta", "Coriolus versicolor",
    "Xerocomus badius", "Chalciporus piperatus", "Scutellinia scutellata",
    "Peziza vesiculosa", "Helvella crispa", "Sarcoscypha coccinea",
    "Rhytisma acerinum", "Taphrina deformans", "Taphrina betulina",
    "Uncinula necator", "Sphaerotheca fuliginea", "Colletotrichum",
    "Sclerotinia sclerotiorum", "Monilinia fructicola", "Diplocarpon rosae",
    "Marssonina", "Septoria", "Cercospora", "Phoma",
    "Amanita caesarea", "Amanita rubescens", "Chlorophyllum molybdites", "Lepiota cristata",
    "Entoloma abortivum", "Ramaria botrytis", "Clavaria zollingeri", "Geastrum triplex",
    "Hypomyces lactifluorum", "Cantharellus cinnabarinus", "Craterellus tubaeformis",
    "Boletus badius", "Leccinum aurantiacum", "Suillus grevillei", "Tricholoma terreum",
    "Clitocybe odora", "Lactarius indigo", "Russula virescens", "Hygrophorus russula",
]

assert len(FUNGI) == 200, f"expected 200 fungi, got {len(FUNGI)}"

if __name__ == "__main__":
    run_batch(FUNGI, file_sink, cooldown=2)
