input_file = open('first_names.txt','r')
line = input_file.readlines()
user_input = 51
n=0
while user_input < 0 or user_input >50:
	user_input = int(input('Enter a number between 0 and 50: '))
	if user_input>0 or user_input <50:
		x = user_input
while n!= x:
	print(line[n])
	n+=1
