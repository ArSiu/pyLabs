import unittest
from technique_manager import TechniqueManager
from technique import InkjetPrinter, LaserPrinter, CuttingPlotter, Shredder
from technique import Companies


class ManagerTest(unittest.TestCase):
    def test_sort(self):
        technique_list = [
            InkjetPrinter("INKJ2000", "3202", Companies.Panasonic, 2019, 299.9, 220, 60, 100, 100, 10),
            LaserPrinter("LP-2040", "4550", Companies.Panasonic, 2020, 200.0, 220, 160, 150, 150),
            CuttingPlotter("CT25", "3542", Companies.Bosh, 2009, 50, 50, 100, "STL 090"),
            Shredder("RoyTom", "model-Y", Companies.Philips, 2007, 30, 220, 200, 12, 24)
        ]
        self.assertEqual(sorted(technique_list, key=lambda technique: technique.price, reverse=True),
                         TechniqueManager(technique_list).sort_by_price(True))
        self.assertEqual(sorted(technique_list, key=lambda technique: technique.price, reverse=False),
                         TechniqueManager(technique_list).sort_by_price(False))
        self.assertEqual(sorted(technique_list, key=lambda technique: technique.name, reverse=True),
                         TechniqueManager(technique_list).sort_by_name(True))
        self.assertEqual(sorted(technique_list, key=lambda technique: technique.name, reverse=False),
                         TechniqueManager(technique_list).sort_by_name(False))
