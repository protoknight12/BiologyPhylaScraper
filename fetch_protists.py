from scraper_engine import run_batch
from main_File import file_sink

# Example bulk-fetch script: scrapes a fixed list instead of prompting interactively.
# Unlike the animal/plant/fungi lists this one isn't 200 long on purpose: Protista is
# almost entirely microorganisms, and there just aren't 200 "well known" species -
# padding further would mean obscure taxa most people (and often Wikipedia) don't
# have much on. This is every protist genuinely recognizable to a non-specialist.
PROTISTS = [
    # Amoebozoa & slime molds
    "Amoeba proteus", "Entamoeba histolytica", "Entamoeba coli", "Naegleria fowleri",
    "Naegleria gruberi", "Acanthamoeba", "Dictyostelium discoideum", "Physarum polycephalum",
    "Fuligo septica", "Chaos carolinense",
    # Ciliates
    "Paramecium caudatum", "Paramecium tetraurelia", "Stentor coeruleus", "Vorticella",
    "Tetrahymena thermophila", "Balantidium coli", "Didinium nasutum", "Euplotes",
    "Colpoda", "Opalina",
    # Flagellates & excavates
    "Euglena viridis", "Euglena gracilis", "Trypanosoma brucei", "Trypanosoma cruzi",
    "Leishmania donovani", "Giardia lamblia", "Trichomonas vaginalis", "Chilomastix mesnili",
    # Apicomplexa
    "Plasmodium falciparum", "Plasmodium vivax", "Plasmodium malariae", "Plasmodium ovale",
    "Toxoplasma gondii", "Cryptosporidium parvum", "Babesia microti", "Theileria",
    "Cyclospora cayetanensis", "Isospora belli",
    # Stramenopiles / oomycetes / algae (chromists, classed as protists)
    "Phytophthora infestans", "Plasmopara viticola", "Saprolegnia", "Diatom",
    "Navicula", "Pinnularia", "Giant kelp", "Bull kelp", "Macrocystis pyrifera",
    "Sargassum", "Fucus vesiculosus", "Laminaria digitata",
    # Dinoflagellates
    "Ceratium", "Noctiluca scintillans", "Pfiesteria piscicida", "Symbiodinium",
    "Karenia brevis",
    # Foraminifera & radiolarians
    "Foraminifera", "Radiolaria", "Globigerina",
    # Green & red algae
    "Spirogyra", "Chlamydomonas reinhardtii", "Volvox", "Ulva lactuca", "Chlorella",
    "Porphyra", "Red algae", "Coralline algae",
    # Other
    "Blastocystis hominis",
]

if __name__ == "__main__":
    run_batch(PROTISTS, file_sink, cooldown=2)
