#heapsort
import random
import time
num_list = []
def GenerateData(num):
    for i in range(num):
        ran = random.randint(0, num)
        num_list.append(ran)
    print("Original: ", num_list) 
    return num_list  
GenerateData(1000000)

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  
# The main function to sort an array of given size 
def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(int(n/2 -1), -1, -1):
        heapify(arr, n, i) 
  
    # One by one extract elements 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

arr = num_list
start = time.time()
heapSort(arr) 
end = time.time()
n = len(arr) 
print("Sorted: ", arr)  
print("Elasped time = " + str(end-start) + " seconds.")