class RetailItem:
    #define class
    def __init__(self, descr, units, price):
        self.descr = descr
        self.units = units
        self.price = price
    #set attributes
    def set_descr(self, descr):
        self.descr = descr
    def set_units(self, units):
        self.units = units
    def set_price(self, price):
        self.price = price
    #return attributes
    def get_descr(self, descr):
        return self.descr
    def get_units(self, units):
        return self.units
    def get_price(self, price):
        return float(self.price)
        
    def __str__(self):
        return "Item description: " + self.descr + \
            "\nUnits in inventory: " + self.units + \
            "\nPrice: " + self.price
#add data
item1 = RetailItem("Jacket", "12", "$59.95")
item2 = RetailItem("Designer Jeans", "40", "$34.95")
item3 = RetailItem("Shirt", "20", "$24.95")

#print data 
print(item1)
print("")
print(item2)
print('')
print(item3)
print('')