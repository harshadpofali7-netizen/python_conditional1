#Program to check exam result 
score = float(input("Enter exam percentage (0-100):"))
if score >= 75:
    result = "distinction"
elif score >= 60:
    result = "first class"
elif score >= 35:
    result = "pass"
else:
    result = "fail"
print("Your exam result is:",result)
