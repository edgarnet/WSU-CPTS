
file = input('Enter file name: ')
input_file= open(file,'r')
lines= input_file.readlines()
total=0
largest=0
smallest=999
average=0
numlines=0
for line in lines:
	print("test")
	line =int(line)
	line=line.strip()
	total = total+line
	numlines=numlines+1
	if line > largest:
		largest=line
	if line < smallest:
		smallest=line
	print('Largest number: ',largest)
	print('Smallest number: ',smallest)
average=float(total/numlines)
print(average)
input_file.close()

###
#
###


