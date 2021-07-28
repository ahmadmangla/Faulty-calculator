num1 = int(input('Please enter 1st number: '))
num2 = int(input('Please enter 2nd number: '))
op = input('Please enter what operation you want to perform: ')

if op == '+':
    print(num1 + num2 + 7)
elif op == '*':
    print(num1 * num2 + 6)
elif op == '/':
    print(num1/num2/3)
elif op == '-':
    print(num1 - num2)
elif op == '%':
    print(num1 % num2)
else:
    print('Please enter a valid operator')

