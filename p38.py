# Program to check whether a student passed all subjects

sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))
sub4 = float(input("Enter marks for Subject 4: "))

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and sub4 >= 40:
    print("✅ The student has passed all subjects.")
else:
    print("❌ The student has not passed all subjects.")