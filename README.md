# Casiofx

Do you like Casio Fx-92+ College calculator algorithmic?
With this tool, you can create these programs in Python!
> [!WARNING]  
> This tool is in beta and will be updated frequently.  
> Please report any bug/enhancement in the issues.

## Default games

By default, you have the following games :

- [Cannon Game](/cannon_game.py)
- [Number Guesser](/number_guesser.py)
- [Rock Paper Scissors](/rock_paper_scissors.py)
- [Tic Tac Toe](/tic_tac_toe.py)

Just play them, and you'll understand the functionning. Enjoy!

## Functions

### Calculator functions

| Function Name         | Description                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------ |
| forward(pixels)       | Forwards of the specified pixels                                                                             |
| rotate(angle)         | Rotates counter-clockwise of the specified angle                                                             |
| goto(x, y)            | Goes to specified coordinates                                                                                |
| penup()               | Raises the pen                                                                                               |
| pendown()             | Lowers the pen                                                                                               |
| stop()                | Kills the window                                                                                             |
| wait()                | Waits 5 seconds                                                                                              |
| lookat(angle)         | Makes arrow look towards specified angle                                                                     |
| comment(text)         | Displays the comment in a pop-up (by default, allowed comments are : 'Yes', 'No', 'Result: ' and 'Number? ') |
| displayResult(result) | Displays the specified int or float through a pop-up                                                         |
| askValue(var)         | Prompts the user for a float value to store in the specified variable                                        |
| asyncMainloop()       | Starts tkinter's mainloop in a thread                                                                        |

### Other functions

| Function Name | Description                                                       |
| ------------- | ----------------------------------------------------------------- |
| RanInt(a, b)  | Generates a random number `n` like `a <= n <= b`                  |
| Ent(number)   | Returns the integer part of the number (similar to `number // 1`) |

## Contributors

Thanks to amolinarius for the module and the games.  
Thanks to cperrier for the cannon_game.py code base.
