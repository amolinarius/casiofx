from module.casiofx import *

calc = Calculator()

# Grid (7x6)
calc.goto(-24.5, 21)
for _ in range(7):
    calc.pendown()
    calc.goto(-calc.x, calc.y)
    calc.penup()
    calc.goto(-calc.x, calc.y-7)
calc.goto(-24.5, 21)
for _ in range(8):
    calc.pendown()
    calc.goto(calc.x, -calc.y)
    calc.penup()
    calc.goto(calc.x+7, -calc.y)
calc.goto(100, 100)

# Stacking
m = 1111111
d = 0
while True:
    a = int(calc.askValue('a')) # Integer needed to avoid overflowerror
    b = 7 - a
    print(a, b)
    c = Ent(m/10**b) - (Ent(m/10**(b+1))*10)
    print(c)
    calc.penup()
    calc.goto(-22.5+7*(a-1), -19+7*(c-1))
    calc.pendown()
    if d == 0:
        calc.goto(calc.x+3, calc.y+3)
        calc.penup()
        calc.goto(calc.x, calc.y-3)
        calc.pendown()
        calc.goto(calc.x-3, calc.y+3)
        d = 1
    else:
        calc.goto(calc.x, calc.y+3)
        calc.goto(calc.x+3, calc.y)
        calc.goto(calc.x, calc.y-3)
        calc.goto(calc.x-3, calc.y)
        d = 0
    calc.penup()
    calc.goto(100, 100)
    m = m + 1*10**b