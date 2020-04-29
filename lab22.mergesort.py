#merge sort
import random
import time

def GenerateData(num):
    num_list = []
    for i in range(num):
        ran = random.randint(0, num)
        num_list.append(ran)
    print("Original: ", num_list) 
    return num_list  
#GenerateData(15)

def mergeSort(arr): 
    #print("Function name = " + __name__)
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array // why are there only 2 elements when divided in half first time?
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        #print("L = " + str(L) + ", R = " + str(R))
        mergeSort(L) # Sorting the first half 
        #print("Merge Left = " + str(L) + ",  R = " + str(R))
        mergeSort(R) # Sorting the second half 
        #print("L = " + str(L) + ",  Merge Right R = " + str(R))

   
        i = j = k = 0

        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
                #print("smaller " + str(arr))
            else: 
                arr[k] = R[j] 
                j+=1
                #print("larger " + str(arr))
            k+=1
          
        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

if __name__ == '__main__': #__main__?
    arr = [7, 15, 2, 11, 10, 6, 9, 5, 15, 0, 3, 12, 7, 3, 8] 
    arr1 = arr.copy()
    start = time.time()
    mergeSort(arr) 
    print("original array = " + str(arr1))
    end = time.time()
    print("Sorted: ", arr) 
    print("Elasped time = " + str(end-start) + " seconds.")