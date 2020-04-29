#coin estimator by weight
p = input("Weight of pennies(in grams): ")
n = input("Weight of nickels(in grams): ")
d = input("Weight of dimes(in grams): ")
q = input("Weight of quarters(in grams): ")

import math
 
p_num = int(p) / 2.5
p_num = round(p_num)
p_rolls = p_num / 50
p_rolls = round(p_rolls)
p_val = p_num * 0.01
print(str(p_rolls) + " red roll(s)")
print(str(p_num) + " pennies")
print("$" + str(p_val) + "\n")

n_num = int(n) / 5
n_num = round(n_num)
n_rolls = n_num / 40
n_rolls = round(n_rolls)
n_val = n_num * 0.05
print(str(n_rolls) + " blue roll(s)")
print(str(n_num) + " nickels")
print("$" + str(n_val) + "\n")

d_num = int(d) / 2.268
d_num = round(d_num)
d_rolls = d_num / 50
d_rolls = round(d_rolls)
d_val = d_num * 0.1
print(str(d_rolls) + " green roll(s)")
print(str(d_num) + " dimes")
print("$" + str(d_val) + "\n")

q_num = int(q) / 5.67
q_num = round(q_num)
q_rolls = q_num / 40
q_rolls = round(q_rolls)
q_val = q_num * 0.25
print(str(q_rolls) + " orange roll(s)")
print(str(q_num) + " quarters")
print("$" + str(q_val) + "\n")