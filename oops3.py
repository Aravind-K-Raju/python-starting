# class pets:
#     def __init__(self,name: str ,age):

#         self.name = name
#         self.age = age
       

#     def show(self):
#         print(f"i am {self.name} of age {self.age}")

#     def speaks(self):
#         print("i dont speak")

# class cat(pets):
#     def __init__(self,name,age,colour):
#         super().__init__(name,age)
#         self.colour = colour

#     def speaks(self):
#         print("meow")

#     def show(self):
#         print(f"i am {self.name} of age {self.age} colour {self.colour}")

# class dog(pets):
#     def speaks(self):
#         print("barks")

# p = pets("hari",12)
# p.show()
# p.speaks()

# c = cat("jack", 11, "white")
# c.show()
# c.speaks()

# d = dog("cups",8)
# d.show()
# d.speaks()

class Item:
    pay_rate = 0.8
    def __init__(self,name: str,price :float,Qty = 0):
        assert price >= 0,f"price {price} is not greater than 0"
        assert Qty >= 0,f"price {Qty} is not greater than 0"
        self.name = name
        self.price = price
        self.Qty = Qty
    
    def total_price(self):
        return self.price*self.Qty
    
    def discount(self):
        self.price = self.price * self.pay_rate #OR Item.pay_rate
    
item1 = Item("Phone",1000,1)
item2 = Item("Adapter",50,3)

print(item1.total_price())
print(item2.total_price())

# Item.pay_rate = 30 #to change the value of class attribute
# print(Item.pay_rate)
# print(item1.pay_rate)
# print(item2.pay_rate)

# print(Item.__dict__) #{'__module__': '__main__', 'pay_rate': 30, '__init__': <function Item.__init__ at 0x000002E4E1349D00>, 'total_price': <function Item.total_price at 0x000002E4E1349C60>, '__dict__': <attribute '__dict__' of 'Item' objects>, '__weakref__': <attribute '__weakref__' of 'Item' objects>, '__doc__': None}
# print(item2.__dict__) #{'name': 'Adapter', 'price': 50, 'Qty': 3}

item1.discount()

print(item1.total_price())
print(item2.total_price())
