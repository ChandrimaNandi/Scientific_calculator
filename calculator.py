#!/usr/bin/env python3
import math
import sys

MENU = '''
Scientific Calculator
---------------------
1) Square root (√x)
2) Factorial (!x)
3) Natural log (ln x)
4) Power (x^b)
5) Exit
Choose an option (1-5): '''

def sqrt(x):
    if x < 0:
        raise ValueError("sqrt: negative input")
    return math.sqrt(x)

def factorial(n):
    if n < 0:
        raise ValueError("factorial: negative input")
    if not float(n).is_integer():
        raise ValueError("factorial: non-integer input")
    return math.factorial(int(n))

def ln(x):
    if x <= 0:
        raise ValueError("ln: non-positive input")
    return math.log(x)

def power(x, b):
    return math.pow(x, b)

def main():
    while True:
        try:
            choice = input(MENU).strip()
            if choice == '1':
                v = float(input('Enter x: '))
                print('√{} = {}'.format(v, sqrt(v)))
            elif choice == '2':
                v = float(input('Enter n (integer): '))
                print('{}! = {}'.format(int(v), factorial(v)))
            elif choice == '3':
                v = float(input('Enter x: '))
                print('ln({}) = {}'.format(v, ln(v)))
            elif choice == '4':
                x = float(input('Enter base x: '))
                b = float(input('Enter exponent b: '))
                print('{}^{} = {}'.format(x, b, power(x, b)))
            elif choice == '5':
                print('Goodbye')
                sys.exit(0)
            else:
                print('Invalid option')
        except Exception as e:
            print('Error:', e)

if __name__ == '__main__':
    main()

