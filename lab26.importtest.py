import audreylib
import time

#arr = [7, 15, 2, 11, 10, 6, 9, 5, 15, 0, 3, 12, 7, 3, 8] 
arr = audreylib.GenerateData(15)

start = time.time()
audreylib.mergeSort(arr) 
end = time.time()
print("Sorted: ", arr) 
print("Elasped time = " + str(end-start) + " seconds.")