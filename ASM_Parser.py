import re
with open('ASM.txt', 'r') as f:
	for line in f:
		line = line.rstrip()
		#print(line)
		if re.search('Active', line):
			if re.search('Not Assigned', line):
				#print(line)
				#check if the last digit is a number or a character (19)
				test123 = line[0:19]
				#print(test123)
				digit = line[18]
				if digit.isdigit():
					port = line[0:19]
					print(port)
				else:
					port = line[0:18]
					print(port)