#menu calculator
print("[1] Chicken Strips - $3.50")
print("[2] French Fries - $2.50")
print("[3] Hamburger - $4.00")
print("[4] Hotdog - $3.50")
print("[5] Large Drink - $1.75")
print("[6] Medium Drink - $1.50")
print("[7] Milk Shake - $2.25")
print("[8] Salad - $3.75")
print("[9] Small Drink - $1.25")
print("Enter your items by the number consecutively.")
cost = 0
order = input("Enter your order: ")
one = order.find("1") #count occurrences
print(one)

if "1" in order:
    cost += 3.5 #just adds 3.5 forever
print(cost)