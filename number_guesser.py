from module.casiofx import *

# Initialization
calc = Calculator()
calc.goto(100, 100)
m = RanInt(0, 200) # Generate number
b = 0 # Number of guesses

while b < 50: # max guesses
    # Question
    a = calc.askValue('a')
    # Verification
    if a > m:
        calc.displayResult(-1)
    if a < m:
        calc.displayResult(1)
    if a == m:
        calc.comment('yes')
        calc.displayResult(b)
        b = 50
    b = b + 1

calc.asyncMainloop()