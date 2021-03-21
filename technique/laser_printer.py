from .printer import Printer
from .technique import Companies
from file import File, Type


class LaserPrinter(Printer):

    def __init__(self, name: str = "", model: str = "", manufactory_company: Companies = None,
                 year_of_manufacture: int = 0, price: float = 0.0, input_voltage: float = 0.0, watts: float = 0.0,
                 amount_of_input_paper: int = 0, amount_of_output_paper: int = 0):

        super().__init__(name, model, manufactory_company, year_of_manufacture, price, input_voltage, watts,
                         amount_of_input_paper, amount_of_output_paper)
        self.__files = list[File(Type.FTPS, "FTPS"), File(Type.SFTP, "SFTP")]
        self.__is_running = True
        self.__is_laser: bool = True

    def __repr__(self):
        return self.__str__()
