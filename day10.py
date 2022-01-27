# create an advanced calculator
num1 = input('please text num1: ')
op = input('please text operator: ')
num2 = input('please text num2: ')
num1 = float(num1)
num2 = float(num2)
if op == '+':
    print(num1 + num2)
elif op == '-':
    print(num1 - num2)
elif op == '*':
    print(num1 * num2)
elif op == '/':
    print(num1 / num2)
else:
    print('please text correct operator')
