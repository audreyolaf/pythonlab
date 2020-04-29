"""
Stage 1:
check existing scores for names
input new names + score into math.txt
"""
d = {}
f = open("math.txt", "r+")
for line in f:
    (key, val) = line.split()
    d[str(key)] = val

while True:
    name = input("Enter name to query: ")
    name = name.capitalize()
    if name in d:
        print(name + "'s score is " + d[name] + ".")
    elif name == "End":
        exit()
    else:
        print(name + "'s score does not exist.")
        new_name = input("Do you want to input the score for " + name + "? (Y/N) ")
        new_name = new_name.capitalize()
        if new_name == "Y":
            score = input("Score: ")
            d[name] = score
            f.write("\r")
            f.write(name + " " + score)
            f.flush()
            print("Successfully appended " + name + "'s score to math.txt.")
        else:
            exit()