##
#  Manage student grades.
#

# Use a dictionary named 'grades' to track student grades.
grades = {}
# code here
while(True):

  # Loop until the user chooses to quit.
  # Check user input for the following "(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? "
  # Prevent unexected inputs by converting input to upper-case
  # code here
  userInput = input("(A)dd, (R)emove, (M)odify, (P)rint all, or (Q)uit? ").upper()

   # Use a condition to handle adding a new student.
   # Convert grade into integer
   # Gather user input for "Enter the name of the student: "
   # Check if student name already exists "Sorry, that student is already present."
   # Gather user input for student grade "Enter the student's grade: "
   # Validate input is in correct format or range, if not notify "Please enter grade as number 0-100"
   # code here
  if userInput == "A":
    studentName = input("Enter the name of the student: ")
    if studentName in grades:
      print("Sorry, that student is already present.")
      continue
    studentGrade = int(input("Enter the student's grade: "))
    if studentGrade >= 0 and studentGrade <= 100:
      grades[studentName] = studentGrade
    else:
      print("Please enter grade as number 0-100")
      continue

   # Handle removing a student if user inputs 'R'
   # Check input for "What student do you want to remove? "
   # use pop to remove key/value form grades
   # see notes https://www.programiz.com/python-programming/methods/dictionary/pop
   # Check if student doesn't exist - "Sorry, that student doesn't exist and couldn't be removed."
   # code here
  elif userInput == "R":
    remove = input("What student do you want to remove? ")
    if remove in grades:
      grades.pop(remove)
    else:
      print("Sorry, that student doesn't exist and couldn't be removed.")
      continue
   # Handle modifying a student grade if user inputs 'M'
   # "Enter the name of the student to modify: "
   # Convert grade into integer
   # If student is in grades dictionary, show existing grade "The old grade is"
   # Gather input for new grade "Enter the new grade: "
   # If student doesn't exist "Sorry, that student doesn't exist and couldn't be modified."
   # code here
  elif userInput == "M":
    modify = input("Enter the name of the student to modify: ")
    if modify in grades:
      print(f"The old grade is: {grades[modify]}")
      grade = int(input("Enter the new grade: "))
      grades[modify] = grade
    else:
      print("Sorry, that student doesn't exist and couldn't be modified.")
      continue
   # Handle printing grade average as a string if user input is 'P'
   # Use "The average grade is "
   # Handle printing all of the student names with associated grade
   # Display explictly as strings
   # code here
  elif userInput == "P":
    avg = 0
    for student in grades:
      avg += grades[student]
    avg = avg / len(grades)
    print(f"The average grade is {avg}")
    for student in grades:
      print(f"{student}: {grades[student]}")
   # Handle the case for quiting if user inputs 'Q' "Goodbye!"
   # code here
  elif userInput == "Q":     
    print("Goodbye!")
    break

   # Handle the case of invalid input. "Sorry, that wasn't a valid choice."
   # code here
  else:
    print("Sorry, that wasn't a valid choice.")
