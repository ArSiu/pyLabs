from technique_manager import TechniqueManager
from technique import InkjetPrinter, LaserPrinter, CuttingPlotter, Shredder
from technique import Companies
from file import File, Type


class example_technique:

    def __init__(self):
        pass

    def start(self):

        tech_manager = TechniqueManager([
            InkjetPrinter("INKJ2000", "3202", Companies.Panasonic, 2019, 299.9, 220, 60, 100, 100, 10),
            LaserPrinter("LP-2040", "4550", Companies.Panasonic, 2020, 200.0, 220, 160, 150, 150),
            CuttingPlotter("CT25", "3542", Companies.Bosh, 2009, 50, 50, 100, "STL 090"),
            Shredder("RoyTom", "model-Y", Companies.Philips, 2007, 30, 220, 200, 12, 24)
        ])

        print("№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№")
        print("\n"+"Sort by name alphabetically reverse"+"\n")
        print("№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№")
        tech_manager.show([Technique for Technique in tech_manager.sort_by_name(True)])
        print("№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№")
        print("\n" + "Sort by name alphabetically" + "\n")
        print("№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№")
        tech_manager.show([Technique for Technique in tech_manager.sort_by_name(False)])
        print("№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№"+ "\n")

        print("################################################")
        print("\n" + "Sort by price from high to low" + "\n")
        print("################################################")
        tech_manager.show([Technique for Technique in tech_manager.sort_by_price(True)])
        print("################################################")
        print("\n" + "sort by price from low to high" + "\n")
        print("################################################")
        tech_manager.show([Technique for Technique in tech_manager.sort_by_price(False)])
        print("################################################"+ "\n")

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        print("\n" + "Search for name INKJ2000s" + "\n")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        tech_manager.search_bar("INKJ2000")
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")






