#!python3
# https://adventofcode.com/2020/day/3

def checkSlope(incX, incY):
    FILENAME = 'day3input.txt'
    puzzleInput = open(FILENAME, 'r')
    map = puzzleInput.readlines()

    width = len(map[0].strip())
    posY = 0
    posX = 0
    trees = 0

    while posY < len(map):
        if map[posY][posX].strip() == '#':
            trees += 1
        posY += incY
        posX = (posX + incX) % width

    return trees

slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)]

solution = 1
for x, y in slopes:
	trees = checkSlope(x, y)
	print('Right ', x, ', down: ', y, ': ',trees , ' trees encountered.')
	solution *= trees 

print('\nPart 2 solutionn: ', solution)
