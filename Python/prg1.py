Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ask(a, b):
	""" This module creates tuples from lines in a text file containing both
	terms and defintions. It then presnts a definition to the user wanting
	the correct term for said defintion."""
	import random
	file = open("/Users/thund/Desktop/flashcards.txt")
	""" open input file"""
	lines = file.readlines()
	""" seperate lines"""
	z = []
	"""create empty list"""
	for x in lines:
		y = tuple(x.strip().split(':'))
		z.append(y)
	"""create tuples and store them in list"""
	x = random.choice(z)
	"""get random definition"""
	print("Definition: ", x[1])
	"""print definition"""
	an = input("What term does this define: ")
	"""get user answer"""
	print(an)
	"print user answer"""
	cor = x[0]
	"""set correct answer"""
	if an.lower() == cor.strip().lower():
		 a += 1
		 b += 1
		 print("Correct!")
		 ask(a, b)
		 """if user answer is the same as the correct answer"""
		 return
	elif an.lower() == "exit":
		print("Total Questions: ", a)
		print("Total Correct: " , b)
		"""if user chooses to exit"""
		return
	else:
		a += 1
		print("Wrong!")
		print("Correct answer: " , cor.lower())
		ask(a, b)
		return

	
>>> i = 0
>>> j = 0
>>> ask(i, j)
Definition:   cannot be changed
What term does this define: immutable
immutable
Correct!
Definition:   implicitly changing the type of a value in order to complete an operation correctly
What term does this define: exit
exit
Total Questions:  1
Total Correct:  1
>>> 
