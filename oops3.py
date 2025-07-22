from Item import Item
from Phone import Phone

phone1 = Phone("vivo",20000,1,4)
phone2 = Phone("samsung",30000,1,2)
phone3 = Phone("oppo",25000,1,1)

for i in range(0,len(Phone.all)):
    print("\n",Phone.all[i])

print("The total number of broken phones from all instances is : ",Phone.total_no_broken_phones())