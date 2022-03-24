import turtle

construtor = turtle.Turtle()

construtor.up()
construtor.back(300)
construtor.down()

raio = 10

for i in range (8):

    construtor.begin_fill()
    construtor.fillcolor('orange')

    construtor.circle(raio)

    construtor.end_fill()

    construtor.up()
    construtor.forward(raio*2.5)
    
    
    
    construtor.down()

    raio = raio*1.3


turtle.done()
