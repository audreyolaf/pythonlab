import time

def Fibonacci(n): 
    if n < 0:
        print("Incorrect input") 
    elif n==0: 
        return 0
    elif n==1: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
#f = open("demofile3.txt", "a")
f = open("C:\\Users\\CF\\demofile3.txt", "w")
f.write("Fibonacci series!\n")
f.flush()
f.write("Written by Audrey\n")
f.flush()
num_times = int(input("Enter a number between 1 and 30: "))
if num_times < 1:
    print ("Please enter a positive number between 1 and 30.")
    quit()
#num_times = 1000

a = [0, 1]
for i in range(2, num_times):
    start = time.time()
    next = a[i-1] + a[i-2]
    a.append(next)
    end = time.time()
    print("Elasped time for i=" + str(i) + ", " + str(end-start) + " seconds.")
    f.write("[" + str(i) + "]: " + str(next))
    f.write("\n")
    #if(i > 10):
    #    break
print (f)
f.close()

f = open("C:\\Users\\CF\\demofile3.txt", "r")
#f = open("demofile3.txt", "r")
print(f.read())