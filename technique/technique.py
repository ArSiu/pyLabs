from enum import Enum


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
