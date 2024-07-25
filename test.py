class ShoppingCart:
    def __init__(self):
        self.cart_quantity = {}
        self.cart_price = {}
    
    def add_price(self, name, price):
        self.cart_price[name] = price
    
    def add_quantity(self, item):
        if item not in self.cart_quantity:
            self.cart_quantity[item] = 1
        else:
            self.cart_quantity[item] += 1

    def total(self):
        total = 0
        for item, quantity in self.cart_quantity.items():
            total += self.cart_price[item] * quantity
        return total

    def len(self):
        total = 0
        for name, item in self.cart_quantity.items():
            total += int(item)
        
        return total

class Item:
    def __init__(self, sc):
        self.sc = sc
    
    def get_price(self, name):
        cart_quantity = self.sc.cart_quantity
        return cart_quantity.get(name, 0)

sc = ShoppingCart()

item = Item(sc)

# Adding prices
for i in range(int(input())):
    name, price = input().split()
    sc.add_price(name, int(price))

for j in range(int(input())):
    command = input()
    if command == 'len':
        print(sc.len())
    elif command == 'total':
        print(sc.total())
    else:
        command, name = command.split()
        sc.add_quantity(name)
