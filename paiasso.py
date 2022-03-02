import turtle
import math

construtorOlhoD = turtle.Turtle()
construtorOlhoE = turtle.Turtle()
construtorNariz = turtle.Turtle()
construtorBoca = turtle.Turtle()

razao = 20


def desenha_olho_e(tart, value):

    tart.speed(90)
    #desenhando o primeiro circulo
    tart.hideturtle()
    tart.begin_fill()
    tart.circle(value)
    tart.end_fill()
    #movimentando turtle
    tart.left(90)
    tart.up()
    tart.forward(razao)
    tart.right(90)
    tart.forward(razao)
    tart.down()
    tart.left(90)

    #desenha o segundo circulo
    tart.color("blue")
    tart.circle(value*2)
    #desenha o terceiro circulo
    tart.circle(value*2.5)
    #desenha o quarto circulo
    tart.circle(value*3)

def desenha_olho_d(tart, value):
    tart.speed(90)
    tart.up()
    tart.forward(2*razao)
    tart.down()
    
    #desenhando o primeiro circulo
    tart.hideturtle()
    tart.begin_fill()
    tart.circle(value)
    tart.end_fill()
    #movimentando turtle
    tart.up()
    tart.left(180)
    tart.forward(razao)
    tart.right(90)
    tart.forward(razao)
    tart.right(180)
    tart.down()
    
    #desenha o segundo circulo
    tart.color("blue")
    tart.circle(value*2)
    #desenha o terceiro circulo
    tart.circle(value*2.5)
    #desenha o quarto circulo
    tart.circle(value*3)    
    
def desenha_nariz(tart, value):
    tart.color("purple")
    tart.hideturtle()
    tart.speed(90)
    tart.up()
    tart.forward(razao)
    tart.right(90)
    tart.forward(razao*4)
    tart.down()

    for i in range(60):
        tart.forward(razao*4)
        tart.right(183)
        
        
def desenha_boca(tart, value):
    tart.color("red")
    tart.pensize(10)
    tart.hideturtle()
    tart.speed(90)
    tart.up()
    tart.forward(razao)
    tart.right(90)
    tart.forward(razao*7)


    
    tart.right(90)
    tart.forward(razao*4)
    tart.left(90)

    tart.down()
    tart.circle(razao*4, 180)

    
desenha_olho_e(construtorOlhoE, razao)

desenha_olho_d(construtorOlhoD, razao)

desenha_nariz(construtorNariz, razao)

desenha_boca(construtorBoca, razao)





