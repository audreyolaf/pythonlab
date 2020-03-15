"""
Stage 2:
changing math.txt -> math.html, score.html, score1.html
styled the table
average + total students
organized parts into functions
"""
def WriteHtmlFile(filename, pd):
    f = open(filename, "w")
    f.write("<html>\n")
    f.write("<table border=\"1\" style=\"text-align:center;vertical-align:middle\">\n")
    f.write("<tr><th colspan=\"2\" bgcolor=\"Plum\">Math Score of Class 2020</th></tr>\n")
    f.flush()
    f.write("<tr><td>Name</td><td>Score</td></tr>\n")
    for k in sorted(pd):
        v = pd[k]
        s = "<tr><td>" + k + "</td><td>" + v + "</td></tr>\n"
        f.write(s)
    a = CalcAvg(pd)
    avg_score = "<tr><td bgcolor=\"LightSkyBlue\">Average</td><td bgcolor=\"LightSkyBlue\">" + str(a) + "</td></tr>\n"
    t = pd.__len__()
    total_stu = "<tr><td bgcolor=\"Gold\">Total Students</td><td bgcolor=\"Gold\">" + str(t) + "</td></tr>\n"
    f.write(avg_score)
    f.write(total_stu)
    f.flush()
    f.write("</table>\n")
    f.write("</html>\n")
    f.flush()
    f.close()

def ReadData(inputfile):
    pd = {}
    f = open(inputfile, "r+")

    for line in f:
        (key, val) = line.split()
        pd[key] = val
    return pd

d = ReadData("math.txt")

def is_valid_score(s):
    try:
        f = float(s)
        if f >= 0 and f <= 200:
            return True
        else:
            return False    
    except ValueError:
        return False

def AppendData(name, score):
    d[name] = score
    f = open("math.txt", "a")
    f.write("\r")
    f.write(name + " " + score)
    f.close()
    print("Successfully appended " + name + "'s score to math.txt.")

def CalcAvg(pd):
    sum = 0.0
    for v in pd.values():
        sum += float(v)
    itemcount = pd.__len__()
    return sum / itemcount

while True:
    name = input("Enter name to query: ")
    name = name.capitalize()
    if name in d:
        print(name + "'s score is " + d[name] + ".")
    elif name == "End":
        exit()
    elif name == "Html":
        WriteHtmlFile("C:\\Apache24\\htdocs\\score.html", d)
        WriteHtmlFile("score1.html", d)
    elif name == "Avg":
        sum = CalcAvg(d)   
        print(sum)     
    else:
        print(name + "'s score does not exist.")
        new_name = input("Do you want to input the score for " + name + "? (Y/N) ")
        new_name = new_name.capitalize()
        if new_name == "Y":
            score = input("Score: ")
            b = is_valid_score(score)
            if b == True:
                AppendData(name, score)
            else:
                print("Invalid Input") 

        else:
            exit()
