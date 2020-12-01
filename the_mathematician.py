#!/usr/local/bin/python3

from re import sub
from random import choice, randrange

def WordCount(x):
	x = x.lower()
	x = sub(r'[^a-z ]+', '', x)
	x = x.split()
	return len(x)

def FixPronouns(theString, subject, possessive):
	theString = sub(r'%%Subj', subject.capitalize(), theString)
	theString = sub(r'%%subj', subject.lower(), theString)
	theString = sub(r'%%Poss', possessive.capitalize(), theString)
	theString = sub(r'%%poss', possessive.lower(), theString)
	return theString

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

otherProjects = ['the square root of two', 'e', 'i', 'tau', 'pi again']

pronouns = [('he', 'his'), ('she', 'her'), ('they', 'their')]
pronouns = choice(pronouns)
ourSubject = pronouns[0]
ourPossessive = pronouns[1]

intro = '\tThe mathematician got up from %%poss project, and sat down at another table. '
intro = intro + '%%Subj needed a break, and decided to write out as many digits of pi %%subj could remember. '
intro = intro + 'Pi was %%poss favorite number. '
intro = intro + '%%Subj picked up %%poss pen, and began to write. "'

outro = '," and at this, %%subj paused. How many digits had %%subj written? '
outro = outro + 'Had anyone memorized that many digits of pi? '
outro = outro + 'Had %%subj made a mistake somewhere in there? '
outro = outro + 'There was no way to tell.'
outro = outro + '\n\t%%Subj decided to stop. '
outro = outro + 'Perhaps next time %%subj would try writing out ' + choice(otherProjects) + ' instead.'

intro = FixPronouns(intro, ourSubject, ourPossessive)
outro = FixPronouns(outro, ourSubject, ourPossessive)

grafIntros=[FixPronouns('."\n\t%%Subj continued to write. "', ourSubject, ourPossessive),
  FixPronouns('."\n\t%%Subj set down %%poss pen, then picked it up and kept writing. "', ourSubject, ourPossessive),
  FixPronouns('."\n\t%%Subj paused for a moment, then went on writing. "', ourSubject, ourPossessive),
  FixPronouns('."\n\t%%Subj sat back, then leaned forward to write some more. "', ourSubject, ourPossessive)]

digitsNeeded = 50000 - (WordCount(intro) + WordCount(outro))

# is this version going to have an error in pi?
errorPct = 34 # this % of text generated will have an error in pi
if (randrange(0, 100) < errorPct):
	# okay, there will be an error. Now to figure out where the error will be
	errorStart = digitsNeeded // 3 # we don't want the error to appear too soon
	errorEnd = digitsNeeded - errorStart # or too close to the end. We want the middle ⅓
	errorLocation = randrange(errorStart, errorEnd)
else:
	errorLocation = -1 # there won't be an error; set location to -1, we'll never see that

# reading in a 1M-byte text file all at once probably isn't the best idea,
# so we're going to read the file one character at a time.

print(intro, end = '')

piFile = open('pi_dec_1m.txt')

grafWords = randrange(100, 500)
while digitsNeeded > 0:
	nextChar = piFile.read(1)
	if nextChar:
		correctDigit = numberToWord[nextChar]
		if (piFile.tell() == 1) or (grafWords == 0):
			correctDigit = correctDigit.capitalize()
		if grafWords == 0:
			beginGraf = choice(grafIntros)
			print(beginGraf, end = '')
			digitsNeeded -= WordCount(beginGraf)
			print(correctDigit, end = ' ')
			grafWords = randrange(50, 300)
		elif digitsNeeded == errorLocation: # this will never be triggered if no error is asked for
			numberList = list(numberToWord.values())
			numberList.remove('point')
			numberList.remove(correctDigit)
			wrongDigit = choice(numberList)
			print(wrongDigit, end = ' ')
		elif (grafWords == 1) or (digitsNeeded == 1):
			print(correctDigit, end = '')
		else:
			print(correctDigit, end = ' ')
	else:
		print('End of file error. I guess pi isn\'t infinite after all! ¯\\_(ツ)_/¯')
		exit(1)
	grafWords -= 1
	digitsNeeded -= 1

piFile.close()

print(outro)

exit(0)