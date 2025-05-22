def swap(a,b):
    b,a = a,b
    print("after swap")
    print(f"a = {a}")
    print(f"b = {b}")

a = int(input("Enter 1st no = "))
b = int(input("Emter 2nd no = "))
print("Before swap")
print(f"a = {a}")
print(f"b = {b}")
swap(a,b)