psum = nsum = zerocount = 0
num = 0

while (num != -1):
    num = int(input("Enter a number:"))

    if (num > 0):
        psum += num
    elif (num < 0 and num != -1):
        nsum += num
    else:
        zerocount += 1

print("Sum of positive numbers:", psum)
print("Sum of negative numbers:", nsum)
print("Count of zeros:", zerocount)