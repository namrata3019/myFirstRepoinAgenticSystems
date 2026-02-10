def EvenOdd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

number = int(input("Enter a number: "))
result = EvenOdd(number)
print("Number is " + result)