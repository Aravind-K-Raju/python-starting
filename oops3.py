import csv

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
    
    @classmethod
    def from_csv(cls):
        with open("Items.csv","r") as f:
            reader = csv.DictReader(f)
            items  = list(reader)
        
        for item in items:
            Item(
                name=item['name'],
                price=float(item['price']),
                Qty=int(item['Qty'])
            )
    
    @staticmethod
    def is_float(num):
        if isinstance(num, float):
            return True
        if isinstance(num, int):
            return False


print(Item.is_float(3))