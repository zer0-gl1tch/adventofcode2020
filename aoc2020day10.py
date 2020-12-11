#!python3
# https://adventofcode.com/2020/day/10

FILENAME = 'day10input.txt'
puzzleInput = open(FILENAME, 'r')
adapters = list(map(int, puzzleInput.readlines()))

adapters.sort()
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)

diff = [0, 0, 0, 0]
for n in range(1, len(adapters)):
    if (adapters[n] - adapters[n-1]) == 1:
        diff[1] += 1
    elif (adapters[n] - adapters[n-1]) == 2:
        diff[2] += 1
    elif (adapters[n] - adapters[n-1]) == 3:
        diff[3] += 1
    else:
        diff[0] += 1

p1s = diff[1] * diff[3]
print('Part 1 solution: ', p1s)

# Part 2 solution thanks to: Aidan Glickman ( https://youtu.be/6Jnf362ee-E )
solutions = [1] + [0] * (len(adapters) - 1)
for i, adapter in enumerate(adapters):
    for j in range(i - 3, i):
        if (adapter - adapters[j]) <= 3:
            solutions[i] += solutions[j]

print('Part 2 solution: ', solutions[-1])
