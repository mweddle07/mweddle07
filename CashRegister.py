from RetailItem import RetailItem
class CashRegister(RetailItem):
    #define class
    def __init__(self):
        self.items = []

    def purchase_item(self, item):
        self.items.append(item)

    def get_total(self):
        total = 0
        for item in self.items:
            total += item.price
        return total

    def show_items(self):
        for item in self.items:
            print("Item:", item.descr)
            print("Price: $", item.price)
            print("")

    def clear(self):
        self.items = []

def main():
    item1 = RetailItem("Jacket", "12", 59.95)
    item2 = RetailItem("Designer Jeans", "40", 34.95)
    item3 = RetailItem("Shirt", "20", 24.95)

    register = CashRegister()

    purchase = True
    while purchase:
        print("1. Purchase Item")
        print("2. Checkout")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("\nRetail Items:")
            print("1. Jacket")
            print("2. Designer Jeans")
            print("3. Shirt")
            item = int(input("Enter the item number: "))
            if item == 1:
                register.purchase_item(item1)
            elif item == 2:
                register.purchase_item(item2)
            elif item == 3:
                register.purchase_item(item3)
        elif choice == 2:
            print("\nYour cart:")
            register.show_items()
            print("Your total: ${:,.2f}". format(register.get_total()))
            purchase = False
        else:
            print("\nItem is unavailable.")
     
main()
