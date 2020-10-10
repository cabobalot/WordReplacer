from PyDictionary import PyDictionary
import sys


dictionary=PyDictionary()

# try:
# 	print(dictionary.meaning('the', disable_errors=True))
# except:
# 	print("fail")

for arg in sys.argv:
	if arg == sys.argv[0]:
		continue
	
	deff = dictionary.meaning(arg, disable_errors=True)
	# print(arg, deff)

	if (not (deff is None)) and ('Noun' in deff):
		print(deff['Noun'][0], end=' ')
	else:
		print(arg, end=' ')

print()

