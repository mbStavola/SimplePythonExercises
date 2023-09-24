numbers = input("Enter numbers to average: ").split()

sum = 0
for number in numbers:
    sum = sum + int(number)

result = sum / len(numbers)

print("Average:", result)