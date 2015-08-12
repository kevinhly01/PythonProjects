# Credit Card Validator using Luhn's Algorithm
# Using Python3
# __author__ = Kevin Ly
# __version__ = 1.0

import sys

def CheckCardValid(digits):
	#print(digits[0])
	# sum python list of odd numbers
	# get last digit and go back two and sum and repeat
	odd_sum = sum(digits[-1::-2])
	even_sum = 0
	for d in digits[-2::-2]:
		even_sum += sum(divmod(d*2,10))
	return (odd_sum + even_sum) % 10

def ValidateAnother():
	print('Do You Want to validate Another credit card? (yes or no)')
	return input().lower().startswith('y')

while True:
	card_num = input('Please enter the credit card number you want to validate \n')
	card_num= list(map(int,card_num))

	print("Credit Card is Valid") if CheckCardValid(card_num) == 0 else print("Credit Card is Invalid")

	if not ValidateAnother():
		sys.exit()