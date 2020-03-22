#bubble sort
import random
num_list = []
def GenerateData(num):
    for i in range(num):
        ran = random.randint(0, num)
        num_list.append(ran)
    print(num_list) 
    
    return num_list  
GenerateData(7)    

def BubbleSort(nums): 
    numnum = len(nums)
    for i in range(numnum):
        for j in range(0, numnum-i-1):
            if nums[j+1] < nums[j]:     
                nums[j], nums[j+1] = nums[j+1], nums[j] 

nums = num_list
BubbleSort(nums)
print(nums)

                