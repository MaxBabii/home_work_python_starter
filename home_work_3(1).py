#Напшите программу калькулятор в которой пользователь сможет выбрать операцию,
#ввести необходимые числа и получить результат.
#Операции, которые необходимо реализовать: сложение, вычитание, умножение, деление, возведение в степень, синус, косинус и тангенс числа



import math

operation = input("""
+
-
*
/
**
sin
cos
tan 
 Select operation:
""")
number_1 = int(input("Enter first number: "))

number_2 = int(input("Enter second number: "))



if operation == "+":
    print("Your result: ", number_1 + number_2)
elif operation == "-":
    print("Your result: ", number_1 - number_2)
elif operation == "*":
    print("Your result: ", number_1 * number_2)
elif operation == "/":
    print("Your result: ", number_1 / number_2)
elif operation == "**":
    print("Your result: ", "power first number:", number_1 ** 2, "   power second number:", number_2 ** 2 )
elif operation == "sin":
    print("Result from the first digit: ", math.sin(number_1))
elif operation == "cos":
    print("Result from the first digit: ", math.cos(number_1))
elif operation == "tg":
    print("Result from the first digit: ", math.tan(number_1))

else:
    print("Error")