#Program to check whether the triangle is equivalen,isosceles or scalene
side1 = float(input("Enter the length of the first side :"))
side2 = float(input("Enter the length of the second side :"))
side3 = float(input("Enter the length of the third side :"))
if (side1 + side2 > side3) and (side1 + side3 > side2) and (side2 + side3 > side1) :
    if side1 == side2 ==side3:
        print("The triangle is an equivalent ")
    elif side1 == side2 or side1 == side3 or side1 == side3 :
        print("The triangle is an isosceles ")
    else:
        print("The triangle is an scalene ")
else:
    print("This side of triangle is not valid")
