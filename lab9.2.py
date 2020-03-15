"""
Stage 3:
use of math.txt + science.txt
add science.txt values using the same names
rounded average
"""
def WriteHtmlFile(filename, dm, ds):
    f = open(filename, "w")
    f.write("<html>\n")
    f.write("<table border=\"1\" style=\"text-align:center;vertical-align:middle\">\n")
    f.write("<tr><th colspan=\"3\" bgcolor=\"Plum\">Student Score of Class 2020</th></tr>\n")
    f.flush()
    f.write("<tr><td>Name</td><td>Math</td><td>Science</td></tr>\n")
    for k in sorted(dm):
        v1 = dm[k]   
        v2 = ds[k]
        s = "<tr><td>" + k + "</td><td>" + v1 + "</td><td>" + v2 + "</td></tr>\n"
        f.write(s)
    
    a = StanDev(dm)
    b = StanDev(ds)
    stand_dev = "<tr><td bgcolor=\"IndianRed\">Standard Deviation</td><td bgcolor=\"IndianRed\">" + str(a) + "</td><td bgcolor=\"IndianRed\">" + str(b) + "</td></tr>\n"
    c = CalcAvg(dm)
    d = CalcAvg(ds)
    avg_score = "<tr><td bgcolor=\"Gold\">Average</td><td bgcolor=\"Gold\">" + str(c) + "</td><td bgcolor=\"Gold\">" + str(d) + "</td></tr>\n"
    t = dm.__len__()
    total_stu = "<tr><td bgcolor=\"LightSkyBlue\">Total Students</td><td bgcolor=\"LightSkyBlue\">" + str(t) + "</td><td bgcolor=\"LightSkyBlue\">" + str(t) + "</td></tr>\n"
    f.write(stand_dev)
    f.write(avg_score)
    f.write(total_stu)
    f.write("</table>\n")
    f.write("</html>\n")
    f.flush()
    f.close()

dm = {}    
ds = {}

def ReadData(inputfile, d):
    f = open(inputfile, "r+")
    d = {}
    for line in f:
        (key, val) = line.split()
        d[key] = val
    return d

md = ReadData("math.txt", dm)
sd = ReadData("science.txt", ds)

def is_valid_score(s):
    try:
        f = float(s)
        if f >= 0 and f <= 200:
            return True
        else:
            return False    
    except ValueError:
        return False

def CalcAvg(md):
    sum = 0.0
    for v1 in md.values():
        sum += float(v1)
    itemcount = md.__len__()
    avrg = sum / itemcount
    avrg = round(avrg, 2)
    return avrg
    for v2 in sd.values():
        sum += float(v2)
    itemcount = sd.__len__()
    avrg1 = sum / itemcount
    avrg1 = round(avrg1, 2)
    return avrg1

def AppendData(filename, d, name, score):   
    d[name] = score
    f = open(filename, "a")
    f.write("\r")
    f.write(name + " " + score)
    f.close()
    print("Successfully appended " + name + "'s score to " + filename) 

def StanDev(d):
    import statistics 
    list = list(d.values())
    for i in range(0, len(list)): 
        list[i] = int(list[i]) 
    s = statistics.stdev(list)
    s = round(s, 2)
    return s
    """
    sci_list = list(sd.values())
    for i in range(0, len(sci_list)): 
        sci_list[i] = int(sci_list[i]) 
    dev1 = statistics.stdev(sci_list)    
    dev1 = round(dev1, 2)         
    return dev1
    """
while True:
    name = input("Enter name to query: ")
    name = name.capitalize()
    #appending values in the txt have stopped working (aka else)
    if name in md:
        sub_name = input("math.txt or science.txt?: ")
        if sub_name == "math.txt":
            print(name + "'s score is " + md[name] + ".")
        elif sub_name == "science.txt":
            print(name + "'s score is " + sd[name] + ".")
        else:
            exit()        
 
    elif name == "End":
        exit()
    elif name == "Html":
        WriteHtmlFile("C:\\Apache24\\htdocs\\score1.html", md, sd)
    elif name == "Avg":
        sum = CalcAvg(md)   
        print("Math: " + str(sum))
        sum = CalcAvg(sd)   
        print("Science: " + str(sum))     
    elif name == "Sd":
        #we got some sd errors...
        std = StanDev(md, std)
        print("Math: " + str(std))    
        std = StanDev(sd, std)
        print("Science: " + str(std))
    else:
        print(name + "'s score does not exist.")
        new_name = input("Do you want to input the score for " + name + "? (Y/N) ")
        new_name = new_name.capitalize()
        if new_name == "Y":
            score = input("Score: ")
            b = is_valid_score(score)
            if b == True:
                file_pick = input("Math or science?: ")
                file_pick.capitalize()
                if file_pick.lower() == "math":
                    AppendDataNew("math.txt", md, name, score)
                if file_pick.lower() == "science":
                    AppendData("science.txt", sd, name, score)
            else:
                print("Invalid Input") 

        else:
            exit()
