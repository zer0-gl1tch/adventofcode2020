#!python3
# https://adventofcode.com/2020/day/11

FILENAME = 'day11input.txt'
puzzleInput = open(FILENAME, 'r')
fp = puzzleInput.read().split()


def searchAdjacents1(floorplan, x, y):
    up = floorplan[y-1][x] if y != 0 else ''
    down = floorplan[y+1][x] if y != (len(floorplan) - 1) else ''
    left = floorplan[y][x-1] if x != 0 else ''
    right = floorplan[y][x+1] if x != (len(floorplan[y]) - 1) else ''
    upL = floorplan[y-1][x-1] if (up != '') and (left != '') else ''
    upR = floorplan[y-1][x+1] if (up != '') and (right != '') else ''
    downL = floorplan[y+1][x-1] if (down != '') and (left != '') else ''
    downR = floorplan[y+1][x+1] if (down != '') and (right != '') else ''

    return [up, down, left, right, upL, upR, downL, downR]


def evolve1(floorplan):
    modFloorplan = []
    for y, line in enumerate(floorplan):
        modLine = ''

        for x, seat in enumerate(line):
            adjacents = searchAdjacents1(floorplan, x, y)

            if (seat == 'L') and ('#' not in adjacents):
                modLine = modLine + '#'
            elif (seat == '#') and (adjacents.count('#') >= 4):
                modLine = modLine + 'L'
            else:
                modLine = modLine + seat

        modFloorplan.append(modLine)

    return modFloorplan


def searchAdjacents2(floorplan, x, y):
    adjacents = 8 * ['.']
    up, down, left, right, upL, upR, downL, downR = adjacents
    i = 1
    while '.' in adjacents:
        if up == '.':
            up = floorplan[y-i][x] if (y-i >= 0) else ''
        if down == '.':
            down = floorplan[y+i][x] if (y+i < len(floorplan)) else ''
        if left == '.':
            left = floorplan[y][x-i] if (x-i >= 0) else ''
        if right == '.':
            right = floorplan[y][x+i] if (x+i < len(floorplan[y])) else ''

        if upL == '.':
            upL = floorplan[y-i][x-i] if (y-i >= 0) and (x-i >= 0) else ''
        if upR == '.':
            upR = floorplan[y-i][x+i] if (y-i >= 0) and (x+i < len(floorplan[y])) else ''
        if downL == '.':
            downL = floorplan[y+i][x-i] if (y+i < len(floorplan)) and (x-i >= 0) else ''
        if downR == '.':
            downR = floorplan[y+i][x+i] if (y+i < len(floorplan)) and (x+i < len(floorplan[y])) else ''
        i += 1

        adjacents = [up, down, left, right, upL, upR, downL, downR]

    return adjacents


def evolve2(floorplan):
    modFloorplan = []
    for y, line in enumerate(floorplan):
        modLine = ''
        for x, seat in enumerate(line):
            adjacents = searchAdjacents2(floorplan, x, y)

            if (seat == 'L') and ('#' not in adjacents):
                modLine = modLine + '#'
            elif (seat == '#') and (adjacents.count('#') >= 5):
                modLine = modLine + 'L'
            else:
                modLine = modLine + seat

        modFloorplan.append(modLine)

    return modFloorplan


def countSeatsOcup(floorplan):
    count = 0
    for line in floorplan:
        count += line.count('#')
    return count


while True:
    part = input('Part 1 or 2?: ')
    if part == '1' or part == '2':
        break
    else:
        print('Please select 1 or 2')

stable = False
i = 1
while stable == False:
    if part == '1':
        newFp = evolve1(fp)
    elif part == '2':
        newFp = evolve2(fp)
    i += 1
    if newFp == fp:
        stable = True
    else:
        fp = newFp

print('Part %s solution: Iteration %i' % (part, i), end=': ')
print(countSeatsOcup(fp))
