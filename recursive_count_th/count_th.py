'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

def count_th(word):
	string = 'th'
	str_length = len( string)

	if len( word) < len( string):					# if word length is less than string length, end
		return 0

	elif word[0: str_length] == string:				# checks for string, by str_length-letter increment
		return 1 + count_th( word[ str_length -1:])	# SUCCESS! return 1 and start over, advancing index by length of string
													# 	( -1 because 0-indexed )
	else:
		return count_th( word[ str_length -1:])		# WOMP WOMP... start over, advancing index by length of string

