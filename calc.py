expr = input(print("2-number expression:"))
parts = expr.split()

num1 = float(parts[0])
op = parts[1]
num2 = float(parts[2])

if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "/":
    result = num1 / num2
else op == "*":
    result = num1 * num2

print(result)
