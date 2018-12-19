from pprint import pprint
import os
import json
import sys

# [X] TODO: We need new DS to store the value of each player that is been thrown in here
# Let's assume that there are only two players.
# This means we can say - P1 = True, P2 = False and default = None
# for each cell there is we can represent it using [True/False/None, num_of_atoms]

cr_grid = [[[None, 0] for i in range(6)] for j in range(9)]


# [X] TODO: Add the marker at certain location (x, y)
def put_weight(user, x, y, split=False):
    if cr_grid[x][y][0] is user or cr_grid[x][y][0] is None or split is True:
        cr_grid[x][y][0] = user
        cr_grid[x][y][1] += 1
    else:
        print("putting weight at another player's cell")
        sys.exit(1)
    check_split(user, x, y)

def clean_cell(x, y):
    cr_grid[x][y][1] = 0
    cr_grid[x][y][0] = None

def split(user, x, y):
    clean_cell(x, y)
    for (i, j) in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]:
        if i >= 0 and i <= 8 and j >= 0 and j <= 5:
            put_weight(user, i, j, split=True)

# [X] TODO: Check if its time to split
def check_split(user, x, y):
    if ((x in [0, 8] and y in [0, 5]) and cr_grid[x][y][1] == 2)\
        or (((x in range(1, 8) and y in [0, 5]) or (x in [0, 8] and y in range(1, 5))) and cr_grid[x][y][1] == 3)\
        or cr_grid[x][y][1] == 4:
        split(user, x, y)

if __name__ == "__main__":
    pprint(cr_grid)
    put_weight(True, 0, 0)
    #    pprint(cr_grid)
    put_weight(False, 0, 5)
    put_weight(False, 8, 0)
    put_weight(False, 0, 0)
    put_weight(False, 8, 5)
    for i in range(3):
        put_weight(True, 4,2)
    for i in range(4):
        put_weight(False, 4,3)
        pprint(cr_grid)
