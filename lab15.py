#mean, median, and mode
num_list = []
import statistics
num_of_num = int(input("How many numbers: "))
for i in range(num_of_num):
    num = int(input("Enter a number: "))
    num_list.append(num) 

def mean():
    s = sum(num_list)
    a = s // len(num_list)
    print("Average: " + str(a))
def median():
    sl = sorted(num_list)
    med = statistics.median(num_list)
    print("Median: " + str(med))    
def mode():
    mode = statistics.mode(num_list)
    print("Mode: " + str(mode))
