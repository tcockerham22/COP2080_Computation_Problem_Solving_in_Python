import grade_compute 

def start():
    return str.upper(input("Enter the 4 letter grades seperated by a '$' or emter Q to quit: "))

def menu(grades_list, avg):
    str = ""
    for letter in grades_list:
        if letter == grades_list[-1]:
            str += letter
        else:
            str += letter + ", "
    final_letter_grade = grade_compute.numberToGrade([avg])
    print(f"----------------------------------------")
    print(f"|         GRADE REPORT SUMMARY         |")
    print(f"----------------------------------------")
    print(f"| Grades Entered: {str}         |")
    print(f"| Lowest Grade Dropped: {grades_list[-1]}              |")
    print(f"| Calculated Average:   {avg}            |")
    print(f"| Final Letter Grade:   {final_letter_grade[0]}              |")
    print(f"----------------------------------------")

def main():
    input = start()
    if input != "Q":
        grades = input.split('$ ')
        number = grade_compute.gradeToNumber(grades)
        number.sort(reverse=True)
        letter = grade_compute.numberToGrade(number)
        avg = average(number)

        menu(letter,avg)

    else:
        print("Goodbye!")

def average(lists):
    avg = 0
    lists.pop(-1)
    for grade in lists:
        avg += grade
    
    return round((avg / len(lists)), 2)

main()