first = int(input("Enter the number: "))
operator = input("+, -, /, * ")
second = int(input("Enter the second number: "))
plus = first + second
minus = first - second
divide = first / second
multiply = first * second
if(operator == "+"):
    print(plus)
elif(operator == "-"):
    print(minus)
elif(operator == "*"):
    print(multiply)
elif(operator == "/"):
    print(divide)