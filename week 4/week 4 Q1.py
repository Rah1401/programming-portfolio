def range(x):
    return 0 <= x <= 100

number = int(input("enter a whole number"))

if range (number):
    print ("true")
else:
    print ("false")
