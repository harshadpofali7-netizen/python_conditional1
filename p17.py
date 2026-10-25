#Program to check grade based on marks (A,B,C,Fail)
marks = float(input("enter the marks (0 to 100) :"))
if marks >= 80 and marks <= 100:
    grade = "A" 
elif marks >= 60 and marks < 80:
    grade = "B" 
elif marks >= 40 and marks < 60:
    grade = "C" 
elif marks >= 0 and marks < 40:
    grade = "Fail"
else: 
    grade = "Invalid marks "

if grade == "Invalid marks ":
    print("Error : please enter a valid mark between 0 to 100.")
else:
    print(f"Your grade is :{grade}")
