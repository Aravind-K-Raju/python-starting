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
        

class Phone (Item):

    all = []
    def __init__(self,name: str,price :float,Qty = 0,broken_phones = 0):
        super().__init__(name,price,Qty)

        assert broken_phones >= 0,f"broken_phones {broken_phones} is not greater than 0"

        self.broken_phones = broken_phones

        Phone.all.append(self)

    @classmethod
    def total_no_broken_phones(cls):
        #the total m=number of broken phones added together from all instances
        return sum(phone.broken_phones for phone in Phone.all)

phone1 = Phone("vivo",20000,1,4)
phone2 = Phone("samsung",30000,1,2)
phone3 = Phone("oppo",25000,1,1)

for i in range(0,len(Phone.all)):
    print("\n",Phone.all[i])

print("The total number of broken phones from all instances is : ",Phone.total_no_broken_phones())