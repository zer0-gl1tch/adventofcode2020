#!python3
# https://adventofcode.com/2020/day/9

FILENAME = 'day9input.txt'
puzzleInput = open(FILENAME, 'r')
inputData = puzzleInput.read().split()

for n in range(25, len(inputData)):
    for prev in inputData[n-25:n]:
        xmas = str(int(inputData[n]) - int(prev)) not in inputData[n-25:n]
        if not xmas:
            break
    if xmas:
        invalidNo = int(inputData[n])
        print('Part 1 solution: ', invalidNo)
        break

suma = 0
contSet = []
offset = 0

while suma != invalidNo:
    suma += int(inputData[offset])
    contSet.append(int(inputData[offset]))
    offset += 1

    while suma > invalidNo:
        suma -= contSet[0]
        del contSet[0]

if suma == invalidNo:
    contSet.sort()
    p2s = contSet[0] + contSet[-1]
    print('Part 2 solution: ', p2s)
