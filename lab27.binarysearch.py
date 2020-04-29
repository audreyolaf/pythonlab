# Python Program for recursive binary search. 

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)//2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            v = binarySearch(arr, l, mid-1, x) #how does calling the function within the function work?
            return v
  
        # Else the element can only be present in right subarray 
        else: 
            v = binarySearch(arr, mid+1, r, x) 
            return v 
  
    else: 
        # Element is not present in the array 
        return -1

def f(n):
    global m
    m = 3
    if(n> 1):
        s = n * f(n-1)
    else:
        s = 1
    return s


m = 5
fm = f(m)
print('factorial of ' + str(m) + '=' + str(fm))

# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 2
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print ("Element is present at index %d" % result) 
else: 
    print ("Element is not present in array")