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

intro = '\tThis is the introduction to the story. "'
outro = '," and that\'s the end of the story.'

digitsNeeded = 1000 - (WordCount(intro) + WordCount(outro))

# is this version going to have an error in π?
errorPct = 34 # this % of text generated will have an error in π
if (randrange(0, 100) < errorPct):
	# okay, there will be an error. Now to figure out where the error will be
	errorStart = digitsNeeded // 3 # we don't want the error to appear too soon
	errorEnd = digitsNeeded - errorStart # or too close to the end. We want the middle 3rd
	errorLocation = randrange(errorStart, errorEnd)
else:
	errorLocation = -1 # there won't be an error; set location to -1, we'll never see that

# reading in a 1M-byte text file all at once probably isn't the best idea,
# so we're going to read the file one character at a time.

print(intro, end = '')

piFile = open('pi_dec_1m.txt')

i = 0
grafWords = randrange(50, 300)
while i < digitsNeeded:
	nextChar = piFile.read(1)
	if nextChar:
		grafWords -= 1
		if grafWords == 0:
			beginGraf = '."\n\tShe continued to write. "'
			print(beginGraf, end = '')
			digitsNeeded -= WordCount(beginGraf)
		correctDigit = numberToWord[nextChar]
		if i == 0 or grafWords == 0:
			print(correctDigit.capitalize(), end = ' ')
			if grafWords == 0:
				grafWords = randrange(50, 300)
		elif i == errorLocation: # this will never be triggered if no error is asked for
			numberList = list(numberToWord.values())
			numberList.remove('point')
			numberList.remove(correctDigit)
			wrongDigit = choice(numberList)
			print(wrongDigit, end = ' ')
		elif i == (digitsNeeded - 1) or grafWords == 1:
			print(correctDigit, end = '')
		else:
			print(correctDigit, end = ' ')
	else:
		print('End of file error. I guess π isn\'t infinite after all! ¯\\_(ツ)_/¯')
		exit(1)
	i += 1

piFile.close()

print(outro)

exit(0)