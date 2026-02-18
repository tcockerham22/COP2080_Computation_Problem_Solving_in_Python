def gradeToNumber(grades_list):
    temp = []
    for letter in grades_list:
        if "A" in letter:
            if "-" in letter:
                temp.append(3.7)
            else:
                temp.append(4)
                
        elif "B" in letter:
            if "+" in letter:
                temp.append(3.3)
            elif "-" in letter:
                temp.append(2.7)
            else:
                temp.append(3)
        elif "C" in letter:
            if "+" in letter:
                temp.append(2.3)
            elif "-" in letter:
                temp.append(1.7)
            else:
                temp.append(2)
        elif "D" in letter:
            if "+" in letter:
                temp.append(1.3)
            elif "-" in letter:
                temp.append(0.7)
            else:
                temp.append(1)
        else:
            temp.append(0)
    return temp

def numberToGrade(grade_list):
    temp = []
    for num in grade_list:
        if num < 0.7:
            temp.append("F")
        elif num < 1:
            temp.append("D-")
        elif num == 1:
            temp.append("D")
        elif num < 1.7:
            temp.append("D+")
        elif num < 2:
            temp.append("C-")
        elif num == 2:
            temp.append("C")
        elif num < 2.7:
            temp.append("C+")
        elif num < 3:
            temp.append("B-")
        elif num == 3:
            temp.append("B")
        elif num < 3.7:
            temp.append("B+")
        elif num < 4:
            temp.append("A-")
        elif num == 4:
            temp.append("A")
    return temp