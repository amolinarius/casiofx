from module.casiofx import *

# Initialization
calc = Calculator()

# Platform
m = RanInt(0, 80)
calc.goto(m, -20.5) # Platform height
calc.pendown()
calc.forward(20) # Platform length
calc.penup()

# Orientation
calc.goto(-60, -19)
b = RanInt(20, 60) # Min and Max angles
calc.lookat(b)
calc.displayResult(b)
a = calc.askValue('a')

# Movement
calc.pendown()
while calc.y > -20:
    calc.forward(a/10)
    calc.rotate(-5)

# Win Detection
if calc.x > m - 2.5: # 2.5 corresponds to treshold
    if calc.x < m + 22.5: # +20 for platform length
        calc.comment('yes')
    else: calc.comment('no')
else: calc.comment('no')
calc.stop()