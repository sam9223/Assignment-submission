
def calculate_grade(marks):
  if marks >= 90:
        return "A+"
  elif 80 <= marks <=89:
        return "A"
  elif 70 <= marks <=79:
        return "B"
  elif 60 <= marks <=69:
        return "C"
  elif 50 <= marks <=59:
        return "D"
  else:
        return "Fail"
    
def get_valid_marks():
  while True:
        try:
            marks = int(input("Enter the marks obtained by the student: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
def main():
    print("Student Grading Program")
    while True:
        marks = get_valid_marks()
        grade = calculate_grade(marks)
        print("The grade for the student is: ",grade)

        choice = input("Do you want to calculate the grade for another student? (y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()

