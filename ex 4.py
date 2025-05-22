def Fahrenheit(c):
    return ((9/5 * c) + 32)

c = int(input("Enter temp in celsius = "))
f = Fahrenheit(c)
print(f)