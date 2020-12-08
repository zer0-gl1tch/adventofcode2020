#!python3
# https://adventofcode.com/2020/day/8

import re, copy

FILENAME = 'day8input.txt'
puzzleInput = open(FILENAME, 'r')
instructions = puzzleInput.readlines()

def runAsembler(instructions):
	opRegex = re.compile(r'(nop|acc|jmp)\s([+-]\d+)')
	executedInstructions = []
	pc = 0
	acc = 0
	while pc not in executedInstructions:
		executedInstructions.append(pc)
		operation = opRegex.search(instructions[pc])
		if operation.group(1) == 'acc':
			acc += int(operation.group(2))
			pc += 1
		elif operation.group(1) == 'jmp':
			pc += int(operation.group(2))
		elif operation.group(1) == 'nop':
			pc += 1
		if pc >= len(instructions):
			break
	return (pc, acc)

print('Part 1 solution: ', runAsembler(instructions)[1])

for i, op in enumerate(instructions):
	modifiedInstructions = copy.copy(instructions)
	if 'jmp' in op:
		modifiedInstructions[i] = 'nop' + instructions[i][3:]
	elif 'nop' in op:
		modifiedInstructions[i] = 'jmp' + instructions[i][3:]
	else:
		continue
	
	pc, acc = runAsembler(modifiedInstructions)
	
	if pc >= len(modifiedInstructions):
		print('Part 2 solution: ', acc)
		break