from .technique import Technique, Companies


class Shredder(Technique):

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0, watts: float = 0.0,
                 amount_of_blades: int = 0, sharpening_of_blades: int = 0):

        super().__init__(name, model, manufactory_company, year_of_manufacture, price, input_voltage, watts)

        self.amount_of_blades = amount_of_blades
        self.sharpening_of_blades = sharpening_of_blades

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Name: {self.name}\n Model:{self.model}\n Manufactory Company: {self.manufactory_company}\n " \
               f"Year of manufacture: {self.year_of_manufacture}\n Price: {self.price}\n " \
               f"Input Voltage: {self.input_voltage}\n Watts: {self.watts}\n " \
               f"Amount of blades: {self.amount_of_blades}\n Sharpening Of Blades: {self.sharpening_of_blades}\n"
