#!python3
# https://adventofcode.com/2020/day/12


class ship:

    compass = ('N', 'E', 'S', 'W')

    def __init__(self, initOr):

        self.x = 0
        self.y = 0
        self.orientation = initOr

    def changeOr(self, newOr):
        self.orientation = self.compass[newOr]

    def changePos(self, direction, distance):
        if direction == 'N':
            self.y += int(distance)
        elif direction == 'S':
            self.y -= int(distance)
        elif direction == 'E':
            self.x += int(distance)
        elif direction == 'W':
            self.x -= int(distance)

    def rotate(self, direction, angle):
        if direction == 'R':
            newOr = int((self.compass.index(self.orientation) + (int(angle) / 90)) % 4)
            self.changeOr(newOr)
        elif direction == 'L':
            newOr = int((self.compass.index(self.orientation) - (int(angle) / 90)) % 4)
            self.changeOr(newOr)

    def advance(self, distance):
        self.changePos(self.orientation, int(distance))


class waypoint(ship):

    def __init__(self, initX, initY):
        self.x = initX
        self.y = initY

    def rotate90R(self):
        temp = self.x
        self.x = self.y
        self.y = -temp

    def rotate(self, direction, angle):
        if direction == 'R':
            for i in range(int(int(angle) / 90) % 4):
                self.rotate90R()
        elif direction == 'L':
            for i in range(4 - int(int(angle) / 90) % 4):
                self.rotate90R()


FILENAME = 'day12input.txt'
puzzleInput = open(FILENAME, 'r')
directions = puzzleInput.read().split()

ferry1 = ship('E')

for direction in directions:
    if direction[0] == 'F':
        ferry1.advance(direction[1:])
    elif direction[0] in ('R', 'L'):
        ferry1.rotate(direction[0], direction[1:])
    elif direction[0] in ferry1.compass:
        ferry1.changePos(direction[0], direction[1])

print('Part 1 solution: ', abs(ferry1.x) + abs(ferry1.y))


ferry2 = ship('E')
wp = waypoint(10, 1)

for direction in directions:
    if direction[0] == 'F':
        ferry2.changePos('E', int(direction[1:]) * wp.x)
        ferry2.changePos('N', int(direction[1:]) * wp.y)
    elif direction[0] in ('R', 'L'):
        wp.rotate(direction[0], direction[1:])
    elif direction[0] in ferry2.compass:
        wp.changePos(direction[0], direction[1])

print('Part 2 solution: ', abs(ferry2.x) + abs(ferry2.y))
