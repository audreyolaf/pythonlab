#quick sort
import random
import time
num_list = []
def GenerateData(num):
    for i in range(num):
        ran = random.randint(0, num)
        num_list.append(ran)
    print("Original: ", num_list) 
    return num_list  
GenerateData(10000)    

def DataArr(num, lower, higher):
    i = lower - 1
    pivot = arr[higher]
    #higher = random.choice(num)
    for j in range(lower, higher):
        if pivot > num[j]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[higher] = arr[higher], arr[i+1]     
    return (i+1)   

def QuickSort(arr, lower, higher): 
    if lower < higher: 
        di = DataArr(arr, lower, higher) 
        QuickSort(arr, lower, di-1) 
        QuickSort(arr, di+1, higher) 

  
arr = num_list
n = len(arr) 
start = time.time()
QuickSort(arr, 0, n-1)
end = time.time()
print("Sorted: ", arr)
print("Elasped time = " + str(end-start) + " seconds.")
