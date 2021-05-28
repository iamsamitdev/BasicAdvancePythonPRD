class Book:

    # Attribute
    # brand = ""
    # price = 0

    # Constructor
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    # Method
    def getDetail(self):
        print("Book name: ", self.brand)
        print("Book price: ", self.price)

    # Destructor
    def __del__(self):
        return 0


