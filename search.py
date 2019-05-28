import difflib
from collections import Counter


inp = open("input.txt","r")
pat = open("patterns.txt")

print(' 1)exactly match\n 2)contain matches\n 3)contain matches with the edit\n ')
choose = input(' Please enter number of mode:')
print('\n------------------')

patterns = pat.read().lower().splitlines()
inputs = inp.read().lower().splitlines()


if choose == '1':
	for pattern in patterns:
		search = difflib.get_close_matches(pattern, inputs, n=len(patterns), cutoff=1)
		if search != []:
			print(search[0])
	print('------------------\n')


elif choose == '2':
	for inp in inputs:
		for pattern in patterns:
			pattern_strings = pattern.split()	
			if all(string in inp for string in pattern_strings):
				print(inp)
	print('------------------\n')


elif choose == '3':
	for pattern in patterns:
		search = difflib.get_close_matches(pattern, inputs, n=len(patterns), cutoff=0.9)
		if search != []:
			print(search[0])
	print('------------------\n')

