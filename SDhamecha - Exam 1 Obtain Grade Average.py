#!/usr/bin/env python3

# display title
print("Obtain Grade Average")
print("======================")

another_student = "y"
while another_student == "y":
    # get number of grades
    num_grades = int(input("How many grades will be entered? "))
    while num_grades <= 0:
        num_grades = int(input("Enter a valid number greater than 0: "))
        
    total = 0
    
    # loop to get each grade 
    for i in range(1, num_grades + 1):
        grade = float(input(f"Enter grade #{i}: "))
        while grade < 0 or grade > 100:
            print("Grade must be from 0 through 100. Try again.")
            grade = float(input(f"Enter grade #{i}: "))
            
        total += grade
        
    average = total / num_grades
    
    # display results
    print("======================")
    print(f"Total Grade Points: {total}")
    print(f"Number of Grades: {num_grades}")
    print(f"Grade Average: {round(average, 2)}")
    print("======================")
    
    # continue choice
    another_student = input("Would you like to enter another student's grades? (y/n): ").lower()
    while another_student != "y" and another_student != "n":
        another_student = input("Invalid input. Enter y or n: ").lower()

print("======================")
print("Completed by, Shivang")