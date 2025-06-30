name = input ("What is your favorite food? ")
print ("My favorite food is",name)
name = input ("What is one of your hobbies? ")
print ("My hobby is",name)
x = 3.4
y = 3.5
z = float(3)
print (x)
print (y)
print (z)
print (x+y+z)

for i in reversed(range(1,11)):
    print (i)

print ("Happy New Year!")

for i in range (1, 21):
    if i == 13:
        continue
    else:
        print (i)


temp = float(input ("What's your temperature?"))

if temp > 37.5:
    print("You have a fever")
elif temp < 36.0:
    print("You're cold")
else:
    print("Your temperature is normal")
