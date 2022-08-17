Name = "Aunri"
Shoe = "Cap and gown 11s"
Maxsize = "13"
Minsize = "7"
Price = "250"
price = 250
MaxSize = 13
MinSize = 7

print("Hi, my name is " + Name + " and I am selling " + Shoe + ".")
print("")
print("Our sizes range from mens " + Minsize + "-" + Maxsize + ".")
size = input("Please enter your shoe size.")
if MinSize <= int(size) <= MaxSize:
    print("We have your size in stock")
else:
    print(
        "Unfortunetly we don't have your size in stock. Please come back another time"
    )
    print("")
print("The price is $" + Price + ".")
wallet = input("Please input how much money you have only using digits.")
print("Wallet: ", int(wallet))
if price > int(wallet):
    print("You do not have enough money. Please try again later.")
else:
    print(
        "One moment please. Your shoe will be brought out to you shortly if your size is still in stock."
    )
