#mean, median, and mode
num_list = []
import statistics
import math

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

def mean():
    mean = statistics.mean(num_list)
    mean = round(mean, 2)
    print("Average: " + str(mean))

def median():
    sl = sorted(num_list)
    med = statistics.median(num_list)
    tn = num_of_num % 2
    if tn == 1:
        print("Median: " + str(med))
    else:
        med_down = int(truncate(med))
        med_up = math.ceil(med)
        if med_up != med_down:
            print("Median: " + str(med_down) + ", " + str(med_up))
        else:
            print("Median: " + str(med))                   
    
def mode():
    try:
            mode = statistics.mode(num_list)
            print("Mode: " + str(mode))
    except statistics.StatisticsError:
            print("There is no unique mode.")   
while True:
    num_of_num = int(input("How many numbers: "))
    for i in range(num_of_num):
        num = int(input("Enter a number: "))
        num_list.append(num) 
    while True:    
        m = input("Mean, median, mode, or exit: ")
        m = m.capitalize()
        if m == "Mean":
            mean()
        elif m == "Median":    
            median()
        elif m == "Mode":    
            mode()
        elif m == "Exit":
            num_list.clear()
            break
        else:
            exit()        