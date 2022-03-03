print ("Using else if condition")

marks = int(input("Student's marks is: "))

if marks >=80:
    print("Student grade is A+")

elif marks >=60:
    print("Student grade is B+")

elif marks >= 40:
    print("Student grade is D+")
    

else:
    print("Student Failed")


if marks >39:
    print("Congratulations")
else:
    print("Try Harder")