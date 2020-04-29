#base converter
user_num = int(input("Enter a number: "))
user_base = int(input("Enter the base: "))
def base10toN(num, base):
    converted_string, modstring = "", ""
    currentnum = num
    if not 1 < base < 17:
        raise ValueError("Base must be between 2 and 16.")
    if not num:
        return '0'
    while currentnum:
        mod = currentnum % base
        currentnum = currentnum // base
        converted_string = chr(48 + mod + 7*(mod > 10)) + converted_string
    print(converted_string)
base10toN(user_num, user_base)    

"""
user_int = int(input("Enter a number: ")) 
user_int = bin(user_int) 
print(user_int)
"""
