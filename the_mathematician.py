#!/usr/local/bin/python3

numberToWord = {'.': 'point', '0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
  '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}

digitsNeeded = 1000

# reading in a 1M-byte text file all at once probably isn't the best idea,
# so we're going to read the file one character at a time.

piFile = open('pi_dec_1m.txt')

for i in range(digitsNeeded):
	nextChar = piFile.read(1)
	if nextChar:
		if i == 0:
			print(numberToWord[nextChar].capitalize(), end = ' ')
		else:
			print(numberToWord[nextChar], end = ' ')
	else:
		print('EOF') # to do: better error checking if this happens
		break

piFile.close()