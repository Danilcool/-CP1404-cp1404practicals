# Laser Maze by 101Comoputing.net - www.101computing.net/laser-maze/
import random, time, os


def drawMaze():
    print("")
    print("    1 2 3 4 5 6 7 8 9 10")
    for i in range(0, 12):
        line = ""
        for j in range(0, 12):
            line = line + maze[i][j]
        if i > 0 and i < 10:
            print(" " + str(i) + line)
        elif i == 0 or i == 11:
            print("  " + line)
        elif i == 10:
            print("10" + line)


def placeBombs(numberOfBombs):
    for i in range(0, numberOfBombs):
        row = random.randint(1, 10)
        col = random.randint(1, 10)
        maze[row][col] = "<>"


def shoot():
    global direction
    state = "shooting"
    row = source[0]
    col = source[1]

    while state == "shooting":
        os.system("cls")
        if direction == "right":
            col = col + 1
        ##Add code here to allow laser to move in all 4 directions

        if maze[row][col] == "  ":
            print("")
            maze[row][col] = "++"
        elif maze[row][col] == "[]":
            print("Exit Gate Reached! Level Cleared!")
            state = "win"
        elif maze[row][col] == "<>":
            print("Laser beam hits a bomb! Game Over!")
            state = "lost"
        elif maze[row][col] == " |" or maze[row][col] == "| " or maze[row][col] == "--":
            print("Laser beam hits a wall! Game Over!")
            state = "lost"
        elif maze[row][col] == ">>":
            print("Laser beam hits it source! Game Over!")
            state = "lost"
        ## Add code here to redirect the laser in a different direction (top, right, bottom, left)  when a reflector wall // or \\ is hit.

        drawMaze()
        time.sleep(0.2)

    # Initialise maze, bombs, laser source and exit gate


maze = [[" -", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "- "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" |", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "| "],
        [" -", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "- "]
        ]

source = (random.randint(1, 10), 0)
direction = "right"
maze[source[0]][source[1]] = ">>"

exit = (random.randint(1, 10), 11)
maze[exit[0]][exit[1]] = "[]"

placeBombs(3)
drawMaze()

##Collect inputs (row and column numbers) to find out where do the user wants to point reflection walls: // and \\
##Add reflection walls to the maze as instructed by the user

shoot()