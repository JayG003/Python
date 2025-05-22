def largest(a,b,c):
    if(a>b and a>c):
        print(f"a = {a} is largest")
    elif(b>a and b>c):
        print(f"b = {b} is largest")
    elif(c>a and c>b):
        print(f"c = {c} is largest")

print("Enter 3 no")
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
largest(a,b,c) 