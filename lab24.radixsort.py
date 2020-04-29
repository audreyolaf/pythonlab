#radix sort
import random
import time
num_list = []
def GenerateData(num):
    for i in range(num):
        ran = random.randint(0, num)
        num_list.append(ran)
    print("Original: ", num_list) 
    return num_list  
GenerateData(100)

def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    # The output array elements that will have sorted arr 
    output = [0] * (n) 
  
    # initialize count array as 0 
    count = [0] * (10) 
  
    # Store count of occurrences in count[] 
    for i in range(0, n): 
        index = (arr[i]/exp1) 
        c = int(index) % 10
        count[c] += 1 #what does this do?
  
    # Change count[i] so that count[i] now contains actual 
    #  position of this digit in output array 
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    # Build the output array 
    i = n-1
    while i>=0: 
        index = (arr[i]/exp1) 
        output[ count[ int((index)%10)]-1] = arr[i] #this line? + below
        count[ int((index)%10) ] -= 1
        i -= 1
  
    # Copying the output array to arr[], 
    # so that arr now contains sorted numbers 
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
  
# Method to do Radix Sort 
def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    # Do counting sort for every digit. Note that instead 
    # of passing digit number, exp is passed. exp is 10^i 
    # where i is current digit number 
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10 
  
# Driver code to test above 
arr = num_list
start = time.time()
radixSort(arr) 
end = time.time()
print("Sorted: ", num_list)
print("Elasped time = " + str(end-start) + " seconds.")
