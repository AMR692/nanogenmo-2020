#!/usr/local/bin/python3

from re import sub

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

digitsNeeded = 1000 - (WordCount(intro) + WordCount(outro))

# reading in a 1M-byte text file all at once probably isn't the best idea,
# so we're going to read the file one character at a time.

print(intro, end = '')

piFile = open('pi_dec_1m.txt')

for i in range(digitsNeeded):
	nextChar = piFile.read(1)
	if nextChar:
		if i == 0:
			print(numberToWord[nextChar].capitalize(), end = ' ')
		elif i == (digitsNeeded - 1):
			print(numberToWord[nextChar], end = '')
		else:
			print(numberToWord[nextChar], end = ' ')
	else:
		print('End of file error. I guess π isn\'t infinite after all! ¯\\_(ツ)_/¯')

piFile.close()

print(outro)