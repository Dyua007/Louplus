stringFind = ''
with open('/tmp/String.txt') as obj:
	oble = obj.read()
	for x in oble:
		if x.isdigit():
			stringFind += x
print(stringFind)

			
