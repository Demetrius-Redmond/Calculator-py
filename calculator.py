def getUserInput():
    user_input = int(input("Enter a number: "))
    return user_input

def getMathematicalOperation():
    operator = input("Enter operator: ")
    return operator

add = lambda num1, num2: num1 + num2
    
subtract = lambda num1, num2: num1 - num2

multiply = lambda num1, num2: num1 * num2

divide = lambda num1, num2: num1 / num2

def calculate():

    num1 = getUserInput()

    operator = getMathematicalOperation()

    num2 = getUserInput()

    match operator:

        case "+":
            answer = add(num1, num2)
            print(f"{num1} plus {num2} equals {answer}")
        case "-":
            answer = subtract(num1, num2)
            print(f"{num1} minus {num2} equals {answer}")
        case "*":
            answer = multiply(num1, num2)
            print(f"{num1} times {num2} equals {answer}")
        case "/":
            answer = divide(num1, num2)   
            print(f"{num1} divided by {num2} equals {answer}")

calculate()