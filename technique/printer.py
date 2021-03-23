from .technique import Technique, Companies
from file import File, Type


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

    def copy_page(self):
        print("Scan copy file")

    def add_file(self, file: File):
        self.get_file.append(file)

    @property
    def get_file(self):
        return self.__files
