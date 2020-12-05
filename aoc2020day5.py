#!python3
# https://adventofcode.com/2020/day/5

FILENAME = 'day5input.txt'
puzzleInput = open(FILENAME, 'r')
seatList = puzzleInput.read().split('\n')


def getId(seat):
    return getRow(seat) * 8 + getCol(seat)


def getRow(seat):
    rows = list(range(128))
    for char in seat[:7]:
        if char == 'F':
            rows = rows[:int(len(rows)/2)]
        elif char == 'B':
            rows = rows[int(len(rows)/2):]
    return rows[0]


def getCol(seat):
    cols = list(range(8))
    for char in seat[7:]:
        if char == 'L':
            cols = cols[:int(len(cols)/2)]
        elif char == 'R':
            cols = cols[int(len(cols)/2):]
    return cols[0]


idList = []
for seat in seatList:
    idList.append(getId(seat))

idList.sort()

print('Part 1 solution: ', idList[-1])

for i in range(idList[0], idList[-1]):
    if i not in idList:
        print('Part 2 solution: ', i)
