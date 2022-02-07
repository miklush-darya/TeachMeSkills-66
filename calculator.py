from cmath import pi
import math


def simple_calculator (x, operatinos_culc, y):
    if operatinos_culc == '+':
        z = x+y
    elif operatinos_culc == '-':
        z = x-y
    elif operatinos_culc == '*':
        z = x*y
    elif operatinos_culc == '/':
        if y == 0:
            print ('enter a different number from 0')
            y_two = float(input('enter number 2: '))
            z = x/y_two
        else:
            z = x/y
    elif operatinos_culc == '%':
        z = x%y
    elif operatinos_culc == '^':
        z = x^y
    else:
        z = 'action not found'
    #final_conc = f"{x} {operatinos_culc} {y} = {z}"
    #print (final_conc)
    print ('=', z)


def engineering_calculator ():

    if operatinos_culc == 'sin':
            what_znach = input ("хотие ввести радианы (1) или значения сторон (2) ? ")

            if what_znach == '1':
                x = float(input('введите значение которое нужно умножить на ПИ : '))
                rad = x*pi
                z = math.sin(rad)                  #в радианах
                final_conc = f"{operatinos_culc}{x}ПИ = {z}"
                print (final_conc)

            elif what_znach == '2':
                x, y = float(input('введите значение противолежащего катета : ')), int(input('введите значение гипотенузы : '))
                z = x/y
                final_conc = f"{operatinos_culc} {x}/{y} = {z}"
                print (final_conc)

    elif operatinos_culc == 'cos':
        what_znach = input ("хотие ввести 1. радианы или 2.значения сторон ? ")

        if what_znach == '1':
            x = float(input('введите значение которое нужно умножить на ПИ : '))
            rad = x*pi
            z = math.cos(rad)                 #в радианах
            final_conc = f"{operatinos_culc}{x}ПИ = {z}"
            print (final_conc)

        elif what_znach == '2':
            x, y = float(input('введите значение прилежащего катета : ')), int(input('введите значение гипотенузы : '))
            z = x/y
            final_conc = f"{operatinos_culc} {x}/{y} = {z}"
            print (final_conc)

    elif operatinos_culc == 'log':
        x, y = float(input('enter number : ')), float(input('введите значение основания : '))
        z = math.log(x, y)
        final_conc = f"{operatinos_culc}{x} по основанию {y} = {z}"
        print (final_conc)

    elif operatinos_culc == 'ln':
        x = float(input('enter number : '))
        z = math.log10(x)
        final_conc = f"{operatinos_culc}{x} = {z}"
        print (final_conc)


while True:
    what_calc = input('Hello! What calculator: 1. engineering or 2. simple ? ')

    if what_calc == '2':
        expression = input('enter expression: ').split()
        a = int(expression[0])
        operatinos_culc = expression[1]
        b = int (expression[2])

        simple_calculator (a, operatinos_culc, b) 
    else:
        operatinos_culc = input('enter action: "sin", "cos", "log", "ln" ')
        if operatinos_culc not in 'sin, cos, log, ln':
                print ('action not found')
                operatinos_culc = input('enter action: "sin", "cos", "log", "ln" ')

        engineering_calculator ()


    n = input('хотите посчитать ещё что-то : y/n ')
    if n == 'y':
        continue
    else:
        print ('good bye')
        break