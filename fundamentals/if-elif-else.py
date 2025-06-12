#write a program that takes an age and tell you if you're able to drive assuming a legal driving age of 16

age = input('Please enter your age to continue>>  ')
age = int(age)

if age > 16:
    print("Great! Here are your car keys")
elif age == 16:
    print("Congrats for finally being old enough to drive")
else:
    print("Oh no, too young!")