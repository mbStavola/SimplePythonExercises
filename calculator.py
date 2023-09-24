first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
operator = input("What operator? ( +, -, *, / ) ")

if operator == "+":
    result = first + second
elif operator == "-":
    result = first - second
elif operator == "*":
    result = first * second
elif operator == "/":
    result = first / second
else:
    print("Unknown operator:", operator)

print(first, operator, second, "=", result)