#Assignment: (Square or Circle)
#
#Description: (draws square or circles)
#
#Author: (Elliott Villars)
#WSU ID: (11463956)
#Completion Time: (3 hours)
#In completing this program, I obtained help or worked with the following:Google
import turtle
import random
while True:
	user_input = input('1: Draw squares\n2: Draw circles')
	if user_input== '1':
		num_square = int(input('Enter the number of squares to draw: '))
		sqr = int(0)
		width = int(input('Enter square width: '))
		col = 0
		while sqr < num_square:
			col = col + 1
			turtle.forward(width)
			turtle.left(90)
			turtle.forward(100)
			turtle.left(90)
			turtle.forward(width)
			turtle.left(90)
			turtle.forward(100)
			turtle.fillcolor(col)
			sqr = sqr + 1
			if sqr >= num_square:
				turtle.bye()
	if user_input == '2':
		num_cir = int(input('Enter the number of circles to draw: '))
		cir = int(0)
		rad = int(input('Enter circle radius: '))
		while cir < num_cir:
			turtle.circle(rad)
			rad = rad-10
			cir = cir +1
			if cir >= num_cir:
				turtle.bye()
#This was even easier than homwork three. I can't really talk about this project.
#This programming assignment went welll. It was pretty easy, 
#I dont have much to say in the topic. other than google was an invaluable asset.
# This excerpt for the first assignment sums up how it went:
#All and all this was not too difficult as I only ran into two problems:
#Keeping track of parenthesis and using proper operands.
#Thank god for friendship and Google (Thank You Casey Hunter).
#This was a  low difficulty project.
#Well these are my thoughts on this assignment
#Didnt shed tears of blood this time.
# Not gonna lie, the reflection essay is the hardest part.
#It was worth.
#I thoughtthat the process was mostly straight-forward.
#Was pretty easy. 
#I am running out of things to say about this.      
#learned many things out of this project
#such as how to use sleep commands and while loops 
#I feel pretty goodd about this assignment.
