def range(x):
    return 0 <= x <= 100

number = int(input("enter a whole number"))

if range (number):
    print ("True:", number, "is in range")
else:
    print ("False", number, "is not in range")
