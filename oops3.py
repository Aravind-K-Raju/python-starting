class Item:
    pay_rate = 0.8
    all = []
    def __init__(self,name: str,price :float,Qty = 0):
        assert price >= 0,f"price {price} is not greater than 0"
        assert Qty >= 0,f"price {Qty} is not greater than 0"

        self.name = name
        self.price = price
        self.Qty = Qty

        #actions to execute
        Item.all.append(self)

    
    def total_price(self):
        return self.price*self.Qty
    
    def discount(self):
        self.price = self.price * self.pay_rate #OR Item.pay_rate

    def __repr__(self):
        return f"Item('{self.name}',{self.price},{self.Qty})"

item1 = Item("Phone", 100, 1)
item2 = Item("Laptop", 1000, 3)
item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)

print(Item.all)
for instance in Item.all:
    print(instance.name)
