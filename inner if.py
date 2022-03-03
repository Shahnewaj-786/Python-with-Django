print("inner if is also known as nested if")

asif = int(input("Total marks of Asif: "))
siam = int(input("Total marks of Siam: "))
joy = int(input("Total marks of Joy: "))

if asif > siam:
    if asif > joy:
        print("First Place goes to Asif")
    else:
        print("First place goes to Joy ")

#if siam > asif:
else: #we can use else also here
    if siam > joy:
        print("First Place goes to Siam")
    else:
        print("First place goes to Joy ")
