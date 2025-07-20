class pets:
    def __init__(self,name: str ,age):

        self.name = name
        self.age = age
       

    def show(self):
        print(f"i am {self.name} of age {self.age}")

    def speaks(self):
        print("i dont speak")

class cat(pets):
    def __init__(self,name,age,colour):
        super().__init__(name,age)
        self.colour = colour

    def speaks(self):
        print("meow")

    def show(self):
        print(f"i am {self.name} of age {self.age} colour {self.colour}")

class dog(pets):
    def speaks(self):
        print("barks")

p = pets("hari",12)
p.show()
p.speaks()

c = cat("jack", 11, "white")
c.show()
c.speaks()

d = dog("cups",8)
d.show()
d.speaks()
