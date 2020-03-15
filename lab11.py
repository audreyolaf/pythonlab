d = {}
s_math = 1
s_science = 2
s_history = 3
s_schoolbus = 4

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

def ReadData(inputfile, d, item):
    f = open(inputfile, "r+")
    for line in f:
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
    WriteData("a_math.txt", s_math, d)
    WriteData("a_science.txt", s_science, d)
    WriteData("a_history.txt", s_history, d)
    WriteData("a_schoolbus.txt", s_schoolbus, d)

WriteAllData(d)