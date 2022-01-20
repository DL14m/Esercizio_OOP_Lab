# How to create a class:

class Item:
    
    all_items = []
    pay_rate = 0.8

    def __init__(self, name:str, price:float, quantity=0):
        #Check price and quantity
        assert price >=0, f"Price {price} is too low!"
        assert quantity >=0, f"Quantity {quantity} is too low!"
        
        #Nota, in alternativa, si possono usare le exceptions
        #if price < 0: 
        #    raise ValueError(f"Price {price} is not greater than or equal to zero!")
        #if quantity < 0: 
        #    raise ValueError(f"Quantity {quantity} is not greater than or equal to zero!")

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all_items.append(self)

    def __repr__(self):
        return f"\nItem:('Product:{self.name}, Price:{self.price}, Quantity:{self.quantity}')"

    def apply_discount(self, price):
        return price * self.pay_rate

    def calculate_total_price(self):
        return self.apply_discount(self.price) * self.quantity

    

# How to create an instance of a class
item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 74.90, 5)

# Calling methods from instances of a class:
print(f"Prezzo totale: {item1.calculate_total_price()}€")
print(f"Prezzo totale: {item2.calculate_total_price()}€")
print(f"Prezzo totale: {item3.calculate_total_price()}€")
print(f"Prezzo totale: {item4.calculate_total_price()}€")
print(f"Prezzo totale: {item5.calculate_total_price()}€")
print(Item.all_items)