a = int(input("Enter a number"))
b = int(input("Enter another number"))
print("1 for Add, 2 for Subtract, 3 for Multiply, 4 for Divide")
c = int(input("Enter your choice"))
if c == 1:
    d = a + b
    print(d)
elif c == 2:
    d = a - b
    print(d)
elif c == 3:
    d = a * b
    print(d)
elif c == 4:
    d = a / b
    print(d)
else:
    print("Invalid Input")
