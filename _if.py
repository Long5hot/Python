n = int(input("Enter a number : "))

if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")


message = "Number is even" if n % 2 == 0 else "Number is Odd"

print(message)