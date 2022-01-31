# How to create a class:

import csv

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

    def tot_price():
        print()
        for i in Item.all_items:
            dictionary = {i.name + " - " + "Prezzo Totale": str(i.calculate_total_price())}
            print(dictionary)

    @staticmethod
    def is_integer(num):
        try:
            int(num)
            return True
        except:
            return False
    
    @classmethod
    def instantiate_from_csv(cls):
        csv_path = r'C:\Users\Utente 39\Documents\temp\github\projects\Esercizio_OOP_Lab\items.csv'
        item = csv.DictReader(open(csv_path), skipinitialspace=True)
        for row in item:
            if Item.is_integer(row['Quantity']):
                print(dict(row))
        return cls

    class Phone:

        def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
            #Check price and quantity
            assert price >=0, f"Price {price} is too low!"
            assert quantity >=0, f"Quantity {quantity} is too low!"
            assert broken_phones >=0, f"Number of Broken Phones {broken_phones} is too low!"
            
            #Nota, in alternativa, si possono usare le exceptions
            #if price < 0: 
            #    raise ValueError(f"Price {price} is not greater than or equal to zero!")
            #if quantity < 0: 
            #    raise ValueError(f"Quantity {quantity} is not greater than or equal to zero!")

            self.name = name
            self.price = price
            self.quantity = quantity
            self.broken_phones = broken_phones

            Item.all_items.append(self)



# How to create an instance of a class
item = Item("Phone", 100, 1)
item = Item("Laptop", 1000, 3)
item = Item("Cable", 10, 5)
item = Item("Mouse", 50, 5)
item = Item("Keyboard", 74.90, 5)


# Calling methods from instances of a class:
#print(Item.instantiate_from_csv(), Item.tot_price())
Item.instantiate_from_csv()
Item.tot_price()
Item.is_integer('')