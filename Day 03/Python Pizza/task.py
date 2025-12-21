print("Welcome to Python Pizza Deliveries!")
pizzaSize = input("What size pizza do you want? S, M or L \n")
print(pizzaSize)
total_bill = 0
match pizzaSize.lower():
    case "s" :
        total_bill += 15
    case "m":
        total_bill += 20
    case "l":
        total_bill += 25
peppercornPizza = input("Do you want pepperoni on your pizza? Y or N: Y \n")
if pizzaSize == "s" and peppercornPizza.lower() == "y":
    total_bill += 2
elif pizzaSize == "m" and peppercornPizza.lower() == "Y" :
    total_bill += 3
cheeseNeeded = input("Do you want extra cheese? Y or N: N \n")
if cheeseNeeded.lower() == "y" :
    total_bill += 1
print(f"Your final bill is: $ {total_bill}")









