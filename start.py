number = int(input("Give me a number ---> :").strip())
check = int(input("Give me another number --> :").strip())

if number % 4 == 0:
    print("Number is even and divisible by four")
elif number % 2 == 0:
    print("Number is even")
elif number % 2 != 0:
    print("Number is odd")

print("Exercise 2")
if number % check == 0:
    print("Division turned even")
elif number % check != 0:
    print("Division turned odd")
