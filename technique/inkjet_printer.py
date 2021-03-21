from .printer import Printer
from .technique import Companies
from file import File


class InkjetPrinter(Printer):

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0, watts: float = 0.0,
                 amount_of_input_paper: int = 0, amount_of_output_paper: int = 0, ammount_of_catriges: int = 0):

        super().__init__(name, model, manufactory_company, year_of_manufacture, price, input_voltage, watts,
                         amount_of_input_paper, amount_of_output_paper)

        self.ammount_of_catriges = ammount_of_catriges

    def __str__(self):
        return f"Name: {self.name}\n Model:{self.model}\n Manufactory Company: {self.manufactory_company}\n " \
               f"Year of manufacture: {self.year_of_manufacture}\n Price: {self.price}\n " \
               f"Input Voltage: {self.input_voltage}\n Watts: {self.watts}\n " \
               f"Input paper: {self.amount_of_input_paper}\n Output Paper: {self.amount_of_output_paper}\n " \
               f"Amount Of Catriges: {self.ammount_of_catriges}\n"

    def __repr__(self):
        return self.__str__()

    def print_pages(self, files: list[File]):
        if self.ammount_of_catriges != 0:
            for i in files:
                print(i)
