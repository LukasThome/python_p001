import turtle
import math

construtor = turtle.Turtle()

x = 100

#desenhando as paredes
construtor.begin_fill()
construtor.fillcolor('darkblue')
for i in range(2):
    construtor.forward(2*x)
    construtor.left(90)
    construtor.forward(x)
    construtor.left(90)

construtor.forward(x/3)
construtor.left(90)

construtor.end_fill()
#desenhando a porta
construtor.begin_fill()
construtor.fillcolor('brown')

construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/3)
construtor.right(90)
construtor.forward(2*x/3)

construtor.end_fill()
#desenhando a janela
##movimentando o construtor sem pintar


construtor.up()  
construtor.left(90)
construtor.forward(x/4)
construtor.left(90)
construtor.forward(x/3)
construtor.down()   

construtor.end_fill()
##Iniciando o desenho
construtor.begin_fill()
construtor.fillcolor('blue')

for i in range(4):
    construtor.forward(x/3)
    construtor.right(90)

construtor.end_fill() 

construtor.up()  
construtor.right(90)
construtor.forward(x/2)
construtor.left(90)
construtor.down()

##contruindo a segunda janela
construtor.begin_fill()
construtor.fillcolor('blue')

for i in range(4):
    construtor.forward(x/3)
    construtor.right(90)

construtor.end_fill()    
#desenhando o telhado
##movimentando o construtor sem pintar


construtor.up()
construtor.forward(2*x/3)
construtor.right(90)
construtor.forward(x/12 + x/2)
construtor.left(135)
construtor.down()


##Iniciando o desenho
construtor.begin_fill()
construtor.fillcolor('cyan')

construtor.forward(x *math.sqrt(2))
construtor.left(90)
construtor.forward(x *math.sqrt(2))

construtor.end_fill()

#Desenhando o beiral
construtor.width(7)
construtor.left(135)
construtor.back(x*0.20)
construtor.forward(x*2+x*0.4)

turtle.done()

###by Lucas Thome da Silva 17207235
