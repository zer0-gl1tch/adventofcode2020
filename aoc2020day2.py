#!python3
# https://adventofcode.com/2020/day/2

import re

FILENAME = 'day2input.txt'
puzzleInput = open(FILENAME, 'r')
inputList = puzzleInput.readlines()

p1 = 0
p2 = 0
pattern = re.compile(r'(\d+)-(\d+)\s(\w):\s(.+)')

for pwd in inputList:
    minL, maxL, letter, password = pattern.findall(pwd)[0]
    if (password.count(letter) >= int(minL)) and (password.count(letter) <= int(maxL)):
        p1 += 1
    if (password[int(minL)-1] == letter) ^ (password[int(maxL)-1] == letter):
        p2 += 1

print('Part1: Valid Passwords: ', p1)
print('Part2: Valid Passwords: ', p2)
