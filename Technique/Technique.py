from enum import Enum
from File.File import File,Type


class Companies(Enum):
    Panasonic = 0
    Bosh = 1
    Philips = 2


class Technique:

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0, watts: float = 0.0):

        self.name = name
        self.model = model
        self.manufactory_company = manufactory_company
        self.year_of_manufacture = year_of_manufacture
        self.price = price
        self.input_voltage = input_voltage
        self.watts = watts

    def __str__(self):
        return f"Name: {self.name}\n Model:{self.model}\n Manufactory Company: {self.manufactory_company}\n " \
               f"Year of manufacture: {self.year_of_manufacture}\n Price: {self.price}\n " \
               f"Input Voltage: {self.input_voltage}\n Watts: {self.watts}\n"


class Printer(Technique):

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0, watts: float = 0.0,
                 amount_of_input_paper: int = 0, amount_of_output_paper: int = 0):

        super().__init__(name, model, manufactory_company, year_of_manufacture, price, input_voltage, watts)
        self.amount_of_input_paper = amount_of_input_paper
        self.amount_of_output_paper = amount_of_output_paper
        self.__files = list[File(Type.FTP, "FTP"), File(Type.FTPS, "FTPS"), File(Type.SFTP, "SFTP")]
        self.__is_running = True

    def __str__(self):
        return f"Name: {self.name}\n Model:{self.model}\n Manufactory Company: {self.manufactory_company}\n " \
               f"Year of manufacture: {self.year_of_manufacture}\n Price: {self.price}\n " \
               f"Input Voltage: {self.input_voltage}\n Watts: {self.watts}\n " \
               f"Input paper: {self.amount_of_input_paper}\n Output Paper: {self.amount_of_output_paper}\n "

    def __repr__(self):
        return self.__str__()

    def turn_on(self, input_voltage: float = 0.0):
        if self.input_voltage <= input_voltage:
            print("Plug on!")

    def turn_off(self):
        print("Plug off!")

    def print_pages(self, files: list[File] = []):
        for i in files:
            print(i)

    def print_on_display(self, message: str = ""):
        print(message)

    def copy(self):
        print("Scan copy File")

    def add_file(self, file: File):
        self.get_file.append(file)

    @property
    def get_file(self):
        return self.__files


class LaserPrinter(Printer):

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0, watts: float = 0.0,
                 amount_of_input_paper: int = 0, amount_of_output_paper: int = 0):

        super().__init__(name, model, manufactory_company, year_of_manufacture, price, input_voltage, watts,
                         amount_of_input_paper, amount_of_output_paper)

        self.__is_laser: bool = True

    def __repr__(self):
        return self.__str__()


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

    def print_pages(self, files: list[File] = []):
        if self.ammount_of_catriges != 0:
            for i in files:
                print(i)


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


class CuttingPlotter(Technique):

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0,
                 watts: float = 0.0, type_of_blade: str = ""):

        super().__init__(name, model, manufactory_company, year_of_manufacture, price, input_voltage, watts)

        self.type_of_blade = type_of_blade

    def __str__(self):
        return f"Name: {self.name}\n Model:{self.model}\n Manufactory Company: {self.manufactory_company}\n " \
               f"Year of manufacture: {self.year_of_manufacture}\n Price: {self.price}\n " \
               f"Input Voltage: {self.input_voltage}\n Watts: {self.watts}\n " \
               f"Type Of blade: {self.type_of_blade}\n"

    def __repr__(self):
        return self.__str__()

    def cut(self):
        print("Cutting")