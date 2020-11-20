#!/usr/local/bin/python3

from re import sub
from random import choice, randrange

def WordCount(x):
	x = x.lower()
	x = sub(r'[^a-z ]+', '', x)
	x = x.split()
	return len(x)

numberToWord = {'.': 'point',
  '0': 'zero',
  '1': 'one',
  '2': 'two',
  '3': 'three',
  '4': 'four',
  '5': 'five',
  '6': 'six',
  '7': 'seven',
  '8': 'eight',
  '9': 'nine'}

intro = 'This is the introduction to the story. "'
outro = '," and that\'s the end of the story.'

digitsNeeded = 100 - (WordCount(intro) + WordCount(outro))

# is this version going to have an error in π?
errorPct = 34 # this % of text generated will have an error in π
hasError = (randrange(0, 100) < errorPct)
if hasError:
	# okay, there will be an error. Now to figure out where the error will be
	errorStart = digitsNeeded // 3 # we don't want the error to appear too soon
	errorEnd = digitsNeeded - errorStart # or too close to the end. We want to be in the middle 3rd
	errorLocation = randrange(errorStart, errorEnd)

# reading in a 1M-byte text file all at once probably isn't the best idea,
# so we're going to read the file one character at a time.

print(intro, end = '')

piFile = open('pi_dec_1m.txt')

for i in range(digitsNeeded):
	nextChar = piFile.read(1)
	if nextChar:
		correctDigit = numberToWord[nextChar]
		if i == 0:
			print(correctDigit.capitalize(), end = ' ')
		elif hasError and i == errorLocation:
			numberList = list(numberToWord.values())
			numberList.remove('point')
			numberList.remove(correctDigit)
			wrongDigit = choice(numberList)
			print(wrongDigit, end = ' ')
		elif i == (digitsNeeded - 1):
			print(correctDigit, end = '')
		else:
			print(correctDigit, end = ' ')
	else:
		print('End of file error. I guess π isn\'t infinite after all! ¯\\_(ツ)_/¯')

piFile.close()

print(outro)