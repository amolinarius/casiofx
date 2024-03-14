from module.casiofx import *

# Initialization
calc = Calculator()
c = 9
d = 1

# Grid
calc.goto(-5, 15)
calc.pendown()
calc.goto(-5, -15)
calc.penup()
calc.goto(5, 15)
calc.pendown()
calc.goto(5, -15)
calc.penup()
calc.goto(-15, 5)
calc.pendown()
calc.goto(15, 5)
calc.penup()
calc.goto(-15, -5)
calc.pendown()
calc.goto(15, -5)
calc.penup()
calc.goto(100, 100)
while c != 0:
    a = calc.askValue('a')
    b = Ent((a - Ent(a)) * 10)
    a = Ent(a)
    calc.goto(-23 + (10*a), 23 - (10*b))
    calc.pendown()
    if d == 1:
        # Cross mode
        calc.goto(calc.x+6, calc.y-6)
        calc.penup()
        calc.goto(calc.x, calc.y+6)
        calc.pendown()
        calc.goto(calc.x-6, calc.y-6)
        d = 2
    else:
        # Square mode
        calc.goto(calc.x+6, calc.y)
        calc.goto(calc.x, calc.y-6)
        calc.goto(calc.x-6, calc.y)
        calc.goto(calc.x, calc.y+6)
        d = 1
    calc.penup()
    calc.goto(100, 100)
    c = c-1

calc.asyncMainloop()