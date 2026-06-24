#elif 

# mini calculator 
ip = int(input("1.Add\n2.Subtract\n3.Multiplication\n4.Division\n5.Power\n6.Exit\n"))

if ip == 6:
    print("You have exited the Calculator!")

else:
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    if ip == 1:
        print("Addition is:", a + b)

    elif ip == 2:
        print("Subtraction is:", a - b)

    elif ip == 3:
        print("Multiplication is:", a * b)

    elif ip == 4:
        if a>0 and b>0:
            print("Division is:", a/b)
        else:
            print("Division not possible by zero!")

    elif ip == 5:
        print("Power is:", a ** b)

    else:
        print("Invalid Input!")

# In C we use swtich key work and in Python we use Match case 

#   Example = 
#   1-5 --> Weekdays 6-7: Weekend inp ip 
ip = int(input("Enter Number to check Day(1-7) ?"))
match ip:
    case 1: print("Weekday")
    case 2: print("Weekday")
    case 3: print("Weekday")
    case 4: print("Weekday")
    case 5: print("Weekday")
    case 6: print("Weekend")
    case 7: print("Weekend")

# Another Method 
ip = int(input("Enter no to check day(1-7) ? "))
match ip: 
    case 1 | 2 | 3 | 4 | 5: print("WeekDay")
    case 6 | 7 : print("Weekend")
    case _: print("Invalid IP")


# Another Example 
ip = int(input("Enter no to check month(1-5)? "))
match ip: 
    case 1 | 2 | 3 | 4 | 5: 
    case _: print("Invalid IP")


# Example 
payment = input("Payment modes are : cash/upi/card \n")

match payment: 
    case "cash": print("cash on delivery is available")
    case "upi" : print("Please enter Upi Id")
    case "Card": print("On card 10% GST included !")
    case _: print("Other payment mode is not available")

    