import turtle

construtor = turtle.Turtle()

x = 100

##Desenhando a estrela

for i in range(4):
    construtor.forward(x)
    construtor.left(145)

construtor.right(x/50)
construtor.forward(x)



turtle.done()
