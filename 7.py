
a = int(input("Enter an integer: "))
b = float(input("Enter a float: "))
c = input("Enter a string: ")
d = bool(int(input("Enter boolean (1=True, 0=False): ")))

print("\nValues and Data Types:")
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))

print("\nArithmetic Operations:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

print("\nString Operations:")
print("Uppercase:", c.upper())
print("Lowercase:", c.lower())
print("Concatenation:", c + " Python")
print("Length:", len(c))
