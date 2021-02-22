class Shoes:
    # static var
    shoe_popular = 0

    # constructor
    def __init__(self, shoeBrand="", shoeCountryManufactoty="", shoeCollection="", shoePrice=0, shoeSize=0, shoeColor=""):
        print("star production of shoes")
        self.shoeBrand = shoeBrand
        self.shoeCountryManufactoty = shoeCountryManufactoty
        self.shoeCollection = shoeCollection
        self.shoePrice = shoePrice
        self.shoeSize = shoeSize
        self.shoeColor = shoeColor
        Shoes.shoe_popular += 1

    # destructor
    def __del__(self):
        pass

    def __str__(self):
        Shoes.shoe_popular += 1
        return f"\nBrand: {self.shoeBrand}\n " \
               f"Country: {self.shoeCountryManufactoty}\n " \
               f"Collection: {self.shoeCollection}\n " \
               f"Price: {self.shoePrice}\n " \
               f"Size: {self.shoeSize}\n " \
               f"Color: {self.shoeColor}\n " \
               f"Popularity: {Shoes.shoe_popular}\n"

    # methonds
    @staticmethod
    def getShabbiness():
        return Shoes.shoe_shabbiness


def main():
    shoes = [Shoes("Abibas", "USA", 12, 40, "Sky blue"),
             Shoes("Nike", "USA", 30, 41, "Dark rock"),
             Shoes("Abraham", "USA", 50, 42, "Кed copper")]
    for shoe in shoes:
        print(shoe)


if __name__ == "__main__":
    main()
