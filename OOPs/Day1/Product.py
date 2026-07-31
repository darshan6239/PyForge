"""
    We have a product
    its name, brand , mfg, exp, gty, price 

    1) print all details of the product
    2) search for a specific product by brand name
    3) Purchase it like you're adding it in a cart 
    4) print its bill
    5) try to download that bill in pdf format and also send it to the particular email of that customer
"""

class products:
    def __init__(self,name,brand,mfg_Date,exp_Date,Qty,Price):
        self.name = name
        self.brand = brand
        self.mfg_Date = mfg_Date
        self.exp_Date = exp_Date
        self.Qty = Qty
        self.Price = Price


product1= products("Parle-G Biscuits", "Parle", "10-01-2026", "10-07-2026", 100, 10)
product2= products("Oreo Vanilla Biscuits", "Oreo", "15-02-2026", "15-08-2026", 80, 30)
product3= products("Aashirvaad Atta", "Aashirvaad", "05-03-2026", "05-03-2027", 50, 320)
product4= products("Tata Salt", "Tata", "20-01-2026", "20-01-2028", 70, 28)
product5= products("MDH Garam Masala", "MDH", "18-02-2026", "18-02-2028", 40, 95)
product6= products("Everest Turmeric Powder", "Everest", "12-01-2026", "12-01-2028", 35, 65)
product7= products("Maggi Noodles", "Nestle", "08-03-2026", "08-09-2026", 120, 14)

x = (product1,product2, product3, product4, product5, product6, product7)

# 3) Purchase every product 
cart = []
while True:
    print("1. To see list\n2. To add item in a cart\n3. Print the bill\n4. EXIT")
    n = int(input("Enter your choice: "))
    b = print("===============")
    match n:
        case 1:
            while True:
                for i in x:
                    print(f"Name = {i.name}\nBrand = {i.brand}\nDate = {i.mfg_Date}\nExp_Date = {i.exp_Date}\nQuantity ={i.Qty}\nPrice = {i.Price}")
                    print("=======================")
                ct = input("Do you want to continue (y/n): ")
                if ct == "y":
                    break

        case 2:
            ch = input("Enter Product Name: ").lower()
            found = False

            for i in x:
                if ch == i.name.lower():
                    cart.append(i)
                    print("Item Added Successfully")
                    found = True
                    break

            if not found:
                print("Item Not Found")

            ct = input("Do you want to continue (y/n): ")
            if ct == "n":
                break

        case 3:
            total = 0

            print("=" * 60)
            print(f"{'Product Name':<30}{'Brand':<15}{'Price':>8}")
            print("=" * 60)

            for item in cart:
                print(f"{item.name:<30}{item.brand:<15}{item.Price:>8}")
                total += item.Price

            print("-" * 60)
            print(f"{'Total':>45}{total:>15}")
            ct = input("Do you want to continue (y/n): ").lower()
            if ct == "n":
                break

        case 4:
            







# 1) Print all the Products Details 
y = (product1,product2, product3, product4, product5, product6, product7)
for i in y:
    print(i.name,i.brand,i.mfg_Date,i.exp_Date,i.Qty,i.Price)


# 2)Search for wheather the product is available or not 
n = input("Enter the brand name: ")
n.title()
found = False
for i in x:
    if n == i.brand:
        print("Your Product is Available")
        found = True
        break
if found == False:
    print("Your Product is not Available!")
