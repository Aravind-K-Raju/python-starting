from Item import Item # first "Item" is the file name (Item.py) an the sencond "Item" is the class name.

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
