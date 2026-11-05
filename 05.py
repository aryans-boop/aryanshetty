name = input("Enter name: ")
usn = input("Enter USN: ")

m1 = int(input("Enter 1st course marks: "))
m2 = int(input("Enter 2nd course marks: "))
m3 = int(input("Enter 3rd course marks: "))

total = m1 + m2 + m3
avg = total / 3

print("\nName:", name)
print("USN:", usn)
print("Total Marks:", total)
print("Average Marks:", avg)

if avg >= 35:
    print("Result: PASS")
else:
    print("Result: FAIL")