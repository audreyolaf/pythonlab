class Solution(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        print ("init")
    def multiply(self):
        mult = int(self.num1) * int(self.num2)
        return mult
    def writefile():
        success_or_not = False
        #write files content
        #if success set success_or_not = true
        #if not success, set success_or_not = false
        return success_or_not
m1 = Solution(2, 3)
m2 = Solution(3,4)
sof = m2.writefile()
if(sof):
    print ("write success")
else :
    print ("write fail")

d = {}
d[1]=m1
d[2]=m2

for i in d:
    print(d[i].multiply())
print("test" )
"""
for i in d:
    print(d) 
#m2.multiply()
"""
