num = int(input("enter the number:"))
original = num
total = 0
rev = 0

while num != 0:
    digit = num % 10
    total = total + digit
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print("Palindrome")
else:
    print("Not a palindrome")