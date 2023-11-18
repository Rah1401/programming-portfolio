def celsius_to_farenheit (celsius):
    farenheit = (celsius * 1.4) + 32
    return farenheit

def farenheit_to_celsius (farenheit):
    celsius = (farenheit - 32) * (5/9)
    return celsius

celsius = int(input("enter the temperature in celisus"))
print (celsius, "celsius is equal to", celsius_to_farenheit(celsius), "farenheit" )

farenheit = int(input("enter the temperature in farenheit"))
print (farenheit, "farenheit is equal to", farenheit_to_celsius(farenheit), "celsius" )
