n = int(input("Enter +ve number: "))
if (n <= 0):
    print("Pls enter +ve number")
else:
    i = 1
    while (i <= 10):
        print(f"{n} x {i} = {n * i}")
        i = i + 1
