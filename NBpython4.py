# #   TUPLES 
# """
# it is immutable 
# it follows indexing 
# allows duplicate
# it cannot change the assigned or cannot updated 
# index start from 0
# round brackets () 
# """

# x = (10,20,30)
# print(type(x))
# print(x[2])

# # to check wheather it is in tuple or not (ELemennt existance)
# x = ("Red", "Pink", "Black")
# print("Red" in x)
# print("Gray" in x)


# # TO check object
# x = (10,20)
# y = (10,20,30)
# x = y 
# print(x is y)

# # packing process 
# x = (10,20,30)
# a,b,c = x
# print(a,b,c)


# # Functions for tuples are - len, max, min, sort, sum 
# # ANd methods are          - count -- number of times it comes in is being counted , index -- particular element ka index return hoga
# a = (10,20,30)
# print(len(a))
# print(a.count(20))
# print(x.index(30))

# # using slicing we want to return
# print(x[1:]) # to print 20 and 30 using slicing 
# print(x[1:2]) # just to print particular element using slicing

# # Nested tuples 
# # b = ((10,20),(30,40))
# # for i in b:
# #     for j in i:         # TO ITERATE THE PARTICULAR ELEMENT 
# #         print(j)    


# c = ((10,20),30,(40,50),"HI")
# for i in c:
#     if type(i) == tuple:
#         for j in i:
#             print(j)
#         continue
#     print(i)

# # Mix nested loop 
# x = [10,[20,30],40,(50,60)]
# print(x[2])
# print(x[3][0])
# print(x[1][1])

# for i in x:
#     if type(i) == list or type(i) == tuple:
#         for j in i:
#             print(j)
#         continue
#     print(i)




# h = (90,"hi",("red", [10,20]), [100,200])
# for i in h:
#     if type(i) == list or type(i) == tuple:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     print(k)
#                 continue
#             print(j)
#         continue
#     print(i)




# Real time applications
#   List to tuple or tuple to list 
# x = (10,30)
# print(type(x))
# y = list(x)
# y.append(40)
# print(y)
# x = tuple(y)
# print(x)

menu = (
    (1, "Panner", 400),
    (2, "CHicken", 600),
    (3, "Desert", 150),
    (4, "Noodles", 200)
)
orders = []
while True:
    #1. View menu , 2. Order , 3. Bill Generation, 4. Exit
    print("What you want to do: \n1.To view menu \n2.To order food \n3.To generate the bill \n4.Exit")
    choice = int(input("Enter your choice: "))
    
    match choice:
        case 1:
            print("    HOTEL MENU CARD")
            for items in menu:
                print(f"items{items[0]}  {items[1]} --> {items[2]}")
        case 2:
            while True:
                item_id = int(input("Please enter the item id: "))
        
                for items in menu:
                    if item_id == items[0]:
                        qty = int(input("Enter the product Quantity : "))
                        orders.append((items[1], items[2], qty))
                print(orders)

                d = int(input("Do you want to order more food: (1-Yes / 0 - no)"))
                if d == 0:
                    break
        case 3:
            total_bill = 0
            print("              -----BILL-----")
            print("ITEM\t\tPRICE\tQty\tAmount")

            tup_orders = tuple(orders)

            for items in tup_orders:
                Name = items[0]
                Price = items[1]
                Qty = items[2]
                Amount = Price*Qty

                print(f"{Name}\t\t{Price}\t{Qty}\t{Amount}")
                total_bill += Amount

            print("           -------------------")
            print("                 Total bill = ",total_bill)

        case 4:
            print("THANK YOU VISIT AGAIN !")
            break
    






