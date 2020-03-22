#bubble sort
import random
import time
num_list = []
def GenerateData(num):
    for i in range(num):
        ran = random.randint(0, num)
        num_list.append(ran)
    print("Original: ", num_list) 
    
    return num_list  
GenerateData(10)    

def BubbleSort(nums): 
    numnum = len(nums)
    start = time.time()
    for x in range(numnum):
        for y in range(0, numnum-x-1):
            if nums[y+1] < nums[y]:     
                nums[y], nums[y+1] = nums[y+1], nums[y] #swap
            print(nums)    
    end = time.time()
    print("Elasped time = " + str(end-start) + " seconds.")

nums = num_list
BubbleSort(nums)
print("Sorted: ", nums)         