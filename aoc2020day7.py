#!python3
# https://adventofcode.com/2020/day/7

import re

FILENAME = 'day7input.txt'
puzzleInput = open(FILENAME, 'r')
rules = puzzleInput.readlines()

def whichOnesCanContain(color):
	global bagsDict
	result = []
	for rule in bagsDict:
		if color in bagsDict[rule].keys():
			result.append(rule)
	for res in result:
		result = result + whichOnesCanContain(res)
	return list(set(result))


def numberBagsInside(color):
	global bagsDict
	result = 0
	for rule in bagsDict[color]:
		result = result + bagsDict[color][rule] + bagsDict[color][rule] * numberBagsInside(rule)
	return result


regexExtBag = re.compile(r'^(.+)\sbags?\scontain')
regexIntBag = re.compile(r'(\d)\s(.+?)\sbags?')

bagsDict = {}

for rule in rules:
	containedBags = {}
	for bagColor in regexIntBag.findall(rule):
		containedBags[bagColor[1]] = int(bagColor[0])

	bagsDict[regexExtBag.search(rule).group(1)] = containedBags

mybag = 'shiny gold'

p1List = whichOnesCanContain(mybag)
print('Part 1 solution: ', len(p1List))

p2res = numberBagsInside(mybag)
print('Part 2 solution: ', p2res)
