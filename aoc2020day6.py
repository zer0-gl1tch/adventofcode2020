#!python3
# https://adventofcode.com/2020/day/6

import copy

FILENAME = 'day6input.txt'
puzzleInput = open(FILENAME, 'r')
gInputs = puzzleInput.read().split('\n\n')

groupAnswers = []
for group in gInputs:
    ans = list(set(group))
    if '\n' in ans:
        ans.remove('\n')
    groupAnswers.append(ans)

p1 = 0
for group in groupAnswers:
    p1 += len(group)

print('Part 1 solution: ', p1)

commonAnswers = []
for index, group in enumerate(groupAnswers):
    groupCommons = copy.copy(group)
    gInputs[index] = gInputs[index].split()
    for ans in group:
        for line in gInputs[index]:
            if ans not in line:
                groupCommons.remove(ans)
                break

    commonAnswers.append(groupCommons)


p2 = 0
for group in commonAnswers:
    p2 += len(group)

print('Part 2 solution: ', p2)
