d = {}

'''
class School():
    def __init__(self, name):
        self.name = name
        self.teachers = {}
class Teacher():
'''

class Student():
    def __init__(self, name):
        self.name = name
        self.id = -1
        self.classno = -1
        self.math = -1
        self.science = -1
        self.history = -1
        self.english = -1
        self.pe = -1
        self.elective = -1
        self.lockernum = -1
        self.schoolbus = -1
        self.address = ""
        self.socialsecuritynumber = 0
        self.myclass = {}
        

def ReadData(inputfile, d, item):
    f = open(inputfile, "r+")
    for line in f:
        if line == "\n":
            continue
        (key, val) = line.split() 
        if key in d:
            s = d[key]
        else:
            s = Student(key)
        if(item.lower()=="math"):
            s.math = val
        if(item.lower()=="science"):
            s.science = val    
        if(item.lower() == "schoolbus"):
            s.schoolbus = val
        if(item.lower() == "history"):   
            s.history = val 
        d[key] = s  

ReadData("math.txt", d, "math") 
ReadData("science.txt", d, "science")
ReadData("schoolbus.txt", d, "schoolbus")
ReadData("history.txt", d, "history")

def WriteConsole(d):
    for k,v in d.items():
        if v.schoolbus == -1:
            sb = "N/A"
        else:
            sb = str(v.schoolbus)
        if v.math == -1:
            m = "N/A"
        else:
            m = str(v.math)   
        if v.science == -1:
            sc = "N/A"
        else:
            sc = str(v.science)
        if v.history == -1:
            h = "N/A"
        else:
            h = str(v.history)                  
        p = str(k) + ": " + m + ", " + sc + ", " + sb + ", " + h + "\n"    
        print(p)

'''
input: score (integer)
output: score string, if score is not -1
        if score is -1, return "N/A"
Usage: a = GetScore(50)  ==> a is "50"
       a = GetScore(-1)  ==> a is "N/A"
'''
def GetScore(score):
    resultstring = ""
    if score == -1:
        resultstring = "N/A"
    else:
        resultstring = str(score)
    return resultstring


def WriteHtmlFile(filename, d):
    f = open(filename, "w")
    f.write("<html>\n")
    f.write("<table border=\"1\" style=\"text-align:center;vertical-align:middle;padding:5px;\">\n")
    f.write("<tr><th colspan=\"5\" bgcolor=\"Plum\">Student Score of Class 2020</th></tr>\n")
    f.flush()
    f.write("<tr><td>Name</td><td>Math</td><td>Science</td><td>History</td><td>Schoolbus</td></tr>\n")
    a = Student("Audrey")
    getattr(a, 'name')
    for k in sorted(d):
        v = d[k]
        if v.math == -1:
            t1 = " "
        else:
            t1 = v.math

        if v.science == -1:
            t2 = " "
        else:
            t2 = v.science

        if v.history == -1:
            t3 = " "
        else:
            t3 = v.history
        
        if v.schoolbus == -1:
            t4 = " "
        else:
            t4 = v.schoolbus
        b = "<tr><td>" + str(v.name) + "</td><td>" + t1 + "</td><td>" + t2 + "</td><td>" + t3 + "</td><td>" + t4 + "</td><tr>"
        f.write(b)
    f.write("</table>\n")
    f.write("</html>\n")
    f.flush()
    f.close()   
s_math = 1
s_science = 2
s_history = 3
s_schoolbus = 4    
def WriteData(filename, subject, d):
    f = open(filename, "w")
    sd = sorted(d)
    for k in sd:
        v = d[k]
        if subject == s_math:
            if int(v.math) == -1:
                continue   
            l = k + " " + v.math
        if subject == s_science:
            if int(v.science) == -1:
                continue   
            l = k + " " + v.science 
        if subject == s_history:
            if int(v.history) == -1:
                continue   
            l = k + " " + v.history       
        if subject == s_schoolbus:
            if int(v.schoolbus) == -1:
                continue   
            l = k + " " + v.schoolbus    
        print(l)
        f.write(l + "\n")
        f.flush()

    f.close()   


def WriteAllData(d):
    WriteData("math.txt", s_math, d)
    WriteData("science.txt", s_science, d)
    WriteData("history.txt", s_history, d)
    WriteData("schoolbus.txt", s_schoolbus, d)


def AppendData(filename, name, score, score_type): 
    ActionFlag = 0  #0 : success, 1: invalid score, 2: fail to write file
    if int(score) < 0:
        print("Invalid score.")
        ActionFlag = 1
        return ActionFlag
    f = open(filename, "a")
    f.write("\r")
    f.write(name + " " + str(score))
    f.close()
    if score_type == 1:
        print("Successfully appended " + name + "'s bus number to " + filename)    
    else:
        print("Successfully appended " + name + "'s score to " + filename)
    return ActionFlag


def Input_Prop(type, score):
    score_input = score
    if score == -1:
        if type == 0:
            score_input = input("Score?: ")
        if type == 1:
            score_input = input("Bus number?: ")
    return score_input

def Output_Prop(name, p):
    if int(p) == -1:
        print(name + " contains no value.")
    else:
        print(name + "'s score is " + str(p) + ".")

def Update_Data(d, name, value, sub_type):
    finish = False
    if name in d:
        o = d[name]
        if sub_type == "math":
            o.math = value
            finish = True
        if sub_type == "science":
            o.science = value
            finish = True
        if sub_type == "schoolbus":
            o.schoolbus = value
            finish = True
    WriteAllData(d)
    return finish

def Delete_Data(d, name):
    finish = True
    v = d.pop(name, None)
    if v == None:
        finish = False
    else:
        WriteAllData(d)    
    return finish
    
"""
#r = Delete_Data(d, "Michael")
r = Update_Data(d, "Michael", "50", "math")
if r :
    print ("Successfully update ")
else :
    print ("No update to current dictionary")

Update_Data(d, "Michael", -1, "bus")
Update_Data(d, "Michael", "80", "science")
"""

def New_Stdnt(d, name): 
    m = input("Math score(-1 if doesn't exist): ")
    sc = input("Science score(-1 if doesn't exist): ")
    sb = input("Schoolbus number(-1 if doesn't exist): ")
    h = input("History score(-1 if doesn't exist): ")
    if m == "-1":
        m = int(m)
    else:    
        f = open("math.txt", "a")
        f.write("\r")    
        f.write(name + " " + str(m))
        f.close()
    if sc == "-1":
        sc = int(sc)
    else:    
        f = open("science.txt", "a")    
        f.write("\r")
        f.write(name + " " + str(sc))
        f.close()
    if sb == "-1":
        sb = int(sb)
    else:
        f = open("schoolbus.txt", "a")    
        f.write("\r")
        f.write(name + " " + str(sb))
        f.close()
    if h == "-1":
        h = int(h)
    else:    
        f = open("history.txt", "a")    
        f.write("\r")
        f.write(name + " " + str(h))
        f.close()
    ReadData("math.txt", d, "math") 
    ReadData("science.txt", d, "science")
    ReadData("schoolbus.txt", d, "schoolbus")
    ReadData("history.txt", d, "history")

'''
Purpose: output somenone's scores/bus number to screen.
function name: QueryData
input parameters: name : name of user
output: name's detail values
return value: false: name not in dictionary
              true: name in dictionary
'''
def QueryData(name):
    name = name.capitalize()
    usernameexists = False
    if name in d:
        s = d[name]
        usernameexists = True
        xm = GetScore(s.math)
        print("----------------")
        print("Name: " + s.name)
        print("Math: " + xm)
        print("Science: " + GetScore(s.science))
        print("Schoolbus: " + GetScore(s.schoolbus))
        print("History: " + GetScore(s.history))
    return usernameexists
def Print_Menu():
    print("[1] Insert")
    print("[2] Update")
    print("[3] Delete")
    print("[4] Query")
    print("[5] Output HTML")
    print("[6] Output Console")
    print("[7] End")

while True:
    Print_Menu()
    selection = input("Choose action: ")
    if selection == "1": #Insert
        name = input("Name to Query: ")
        if name in d:
            transition = input(name + " exists, do you want to update the scores?(Y/N) ")
            transition = transition.capitalize()
            if transition == "Y":
                sub_type = input("Math, science, history, or schoolbus?: ")
                if sub_type == "schoolbus":
                    value = input("Bus number: ")
                else:
                    value = input("Score: ")
                Update_Data(d, name, value, sub_type)
            if transition == "N":    
                quit()   
        else:
            New_Stdnt(d, name)    
    elif selection == "2": #Update
        name = input("Name to Query: ")
        name = name.capitalize()
        if name in d:
            sub_type = input("math, science, schoolbus, or history?: ")
            if sub_type == "schoolbus":
                value = input("Bus number: ")  
                Update_Data(d, name, value, sub_type)
                print("Update complete.")  
            else:
                value = input("Score: ")  
                Update_Data(d, name, value, sub_type)
                print("Update complete.")    
        else:
            print("No changes have been made.")    
    elif selection == "3": #delete
        name = input("Student Name: ")
        name = name.capitalize()
        NameExist = QueryData(name)
        if NameExist == True:
            check = input("Are you sure you want to delete " + name + " (Y/N)?: ")
            if check == "Y" or check == "y":
                Delete_Data(d, name)
                print("Delete complete.")
            else:
                print("*** There has been no modification. ***\n")    
        else:
            print("Name does not exist.")            
    elif selection == "4": #Query
        name = input("Name to Query: ")
        QueryData(name)
    elif selection == "5": #Output HTML"
        WriteHtmlFile("C:\\Apache24\\htdocs\\score2.html", d)
        print("Html complete.")
    elif selection == "6": #Output Console
        WriteConsole(d)
    elif selection == "7":
        exit()    

        



