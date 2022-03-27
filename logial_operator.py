num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
num3 = input("Enter 3rd number: ")

if num1>num2 and num1>num3:
    print("Top is: ",num1)

elif num2>num1 and num2>num3:
    print("Top is: ",num2)
else:
    print("Top is: ",num3)