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
    def __init__(self,name: str,price :float,Qty = 0):
        assert price >= 0,f"price {price} is not greater than 0"
        assert Qty >= 0,f"price {Qty} is not greater than 0"
        self.name = name
        self.price = price
        self.Qty = Qty
    
    def total_price(self):
        return self.price*self.Qty
    
item1 = Item("Phone",1000,1)
item2 = Item("Adapter",50,3)

print(item1.total_price())
print(item2.total_price())
