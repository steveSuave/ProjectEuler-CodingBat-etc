import turtle

def equi(side):
	for i in range(3):
		turtle.forward(side)
		turtle.left(120)

def sierp(line,depth):
	equi(line)
	if depth==0:
		return
	turtle.forward(line/2)
	turtle.left(120)
	sierp(line/2, depth-1)
	turtle.forward(line/2)
	turtle.right(120)
	sierp(line/2, depth-1)
	turtle.forward(line/2)
	turtle.right(120)
	sierp(line/2, depth-1)
	turtle.forward(line/2)
	turtle.right(60)
	turtle.forward(line/2)
	turtle.right(180)
	

myWin = turtle.Screen()

turtle.shape("turtle")
turtle.up()
turtle.goto(-300,-300)
turtle.down()
turtle.speed(0)
turtle.pensize(4)
sierp(600,5)

myWin.exitonclick()

	
		