#!python3
# https://adventofcode.com/2020/day/4

import re


def isvalid1(passport):

    validKeys = [
        'byr',  # (Birth Year)
        'iyr',  # (Issue Year)
        'eyr',  # (Expiration Year)
        'hgt',  # (Height)
        'hcl',  # (Hair Color)
        'ecl',  # (Eye Color)
        'pid',  # (Passport ID)
        # 'cid',  # (Country ID)
    ]

    valid = True
    for k in validKeys:
        if k not in passport.keys():
            valid = False
            break
    return valid


def isvalid2(passport):
    '''Part 2:
      byr (Birth Year) - four digits; at least 1920 and at most 2002.
      iyr (Issue Year) - four digits; at least 2010 and at most 2020.
      eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
      hgt (Height) - a number followed by either cm or in:
          If cm, the number must be at least 150 and at most 193.
          If in, the number must be at least 59 and at most 76.
      hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
      ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
      pid (Passport ID) - a nine-digit number, including leading zeroes.
      cid (Country ID) - ignored, missing or not.
    '''
    valid = isvalid1(passport)
    if valid:
        xyrRegex = re.compile(r'^\d{4}$')
        hgtRegex = re.compile(r'^(1\d{2})(cm)$|^(\d{2})(in)$')
        hclRegex = re.compile(r'^#[\dabcdef]{6}$')
        eclRegex = re.compile(r'^amb$|^blu$|^brn$|^gry$|^grn$|^hzl$|^oth$')
        pidRegex = re.compile(r'^\d{9}$')

        if xyrRegex.search(passport['byr']) == None:
            valid = False
        elif (int(passport['byr']) < 1920) or (int(passport['byr']) > 2002):
            valid = False

        if xyrRegex.search(passport['iyr']) == None:
            valid = False
        elif (int(passport['iyr']) < 2010) or (int(passport['iyr']) > 2020):
            valid = False
        
        if xyrRegex.search(passport['eyr']) == None:
            valid = False
        elif (int(passport['eyr']) < 2020) or (int(passport['eyr']) > 2030):
            valid = False

        hgtMatch = hgtRegex.search(passport['hgt'])
        if hgtMatch == None:
            valid = False
        elif hgtMatch.group(2) == 'cm':
            if (int(hgtMatch.group(1)) < 150) or (int(hgtMatch.group(1)) > 193):
                valid = False
        elif hgtMatch.group(2) == 'in':
            if (int(hgtMatch.group(1)) < 59) or (int(hgtMatch.group(1)) > 76):
                valid = False

        if hclRegex.search(passport['hcl']) == None:
            valid = False

        if eclRegex.search(passport['ecl']) == None:
            valid = False

        if pidRegex.search(passport['pid']) == None:
            valid = False

    return valid


FILENAME = 'day4input.txt'
puzzleInput = open(FILENAME, 'r')
passportList = puzzleInput.read().split('\n\n')

fieldPattern = re.compile(r'(\w{3}):(\S+)')
passportStruct = []

for passport in passportList:
    fields = fieldPattern.findall(passport)
    p = {}
    for f in fields:
        p[f[0]] = f[1]
    passportStruct.append(p)

validsP1 = 0
validsP2 = 0
for passport in passportStruct:
    if isvalid1(passport):
        validsP1 += 1
    if isvalid2(passport):
        validsP2 += 1

print('Part 1 solution: ', validsP1)
print('Part 2 solution: ', validsP2)
