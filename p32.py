# Program to check exam eligibility based on attendance and marks

attendance = float(input("Enter your attendance percentage: "))
marks = float(input("Enter your marks: "))

if attendance >= 75:   
    if marks >= 40:    
        print("✅ The student is eligible for the exam.")
    else:
        print("❌ The student is not eligible: Marks are below 40.")
else:
    print("❌ The student is not eligible: Attendance is below 75%.")