#loop

#while_loop

i = 2
while i<=100:
    print(i)
    i = i+2

print("Program End")

i = 1
while i<=100:
    print(i)
    i = i+2

print("Program End")


#sum of 1 to 100

j = 1
sum =0
while j<=200:
    sum = sum+j
    j=j+1

print(sum)
print("Program End")

##break continue

i = 1
while i<=100:
    if i == 20:
        break
    print(i)
    i = i+1

print("Program End")

i = 1
while i<=100:
    print(i)
    i = i+1
    if i == 20:
        continue

print("Program End")