from technique.technique import Technique


class TechniqueManager:

    def __init__(self, tech: list[Technique] = None):
        self.tech = tech

    def add_technique(self, technique: Technique = None):
        self.tech.append(technique)

    def get_technique(self, index: int = 0):
        return self.tech[index]

    def sort_by_name(self, reverse: bool = False):
        return sorted(self.tech, key=lambda technique: technique.name, reverse=reverse)

    def sort_by_price(self, reverse: bool = False):
        return sorted(self.tech, key=lambda technique: technique.price, reverse=reverse)

    def search_bar(self, in_put: str = ""):
        for i in self.tech:
            if i.name == in_put:
                print(i)
                break

    def show(self, tech: list[Technique] = None):
        if tech is not None:
            for i in tech:
                print(i)
        else:
            for i in self.tech:
                print(i)
