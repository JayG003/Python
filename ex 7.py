import numpy as n
def Area(r):
    a = n.pi*(r**2)
    print(f"{a} is the are of circe with redius {r}")

r = int(input("Enter the redius of circle = "))
Area(r)