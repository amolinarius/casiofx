from module.casiofx import *

# Initialization
calc = Calculator()

# Median line
calc.goto(0, 25)
calc.pendown()
calc.goto(calc.x, -25)
calc.penup()
calc.goto(100, 100)

# Make players choose item
m = 0
for _ in range(0, 2):
    b = calc.askValue('b')
    if m == 0:
        a = b
    m = m + 1
f = 0
m = 0
calc.wait()
for _ in range(0, 2):
    if m == 0:
        f = a
        calc.goto(-30, 10)
    else:
        f = b
        calc.goto(10, 10)
    calc.pendown()
    if f == 0:
        calc.goto(calc.x+20, calc.y)
        calc.goto(calc.x, calc.y-20)
        calc.goto(calc.x-20, calc.y)
        calc.goto(calc.x, calc.y+20)
    if f == 1:
        calc.penup()
        calc.goto(calc.x, -10)
        calc.pendown()
        calc.goto(calc.x+5, calc.y+20)
        calc.goto(calc.x+15, calc.y)
        calc.goto(calc.x-5, calc.y-20)
        calc.goto(calc.x-15, calc.y)
    if f == 2:
        calc.goto(calc.x+20, calc.y-20)
        calc.penup()
        calc.goto(calc.x, calc.y+20)
        calc.pendown()
        calc.goto(calc.x-20, calc.y-20)
    m = m + 1
    calc.penup()
    calc.goto(100, 100)

calc.asyncMainloop()