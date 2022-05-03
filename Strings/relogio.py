import turtle
import math



construtorBorda = turtle.Turtle()
construtorPonteiroH = turtle.Turtle()
construtorPonteiroM = turtle.Turtle()
construtorPonteiroS = turtle.Turtle()
construtorMarcadores = turtle.Turtle()

razao = 150
def desenha_borda(tart):
    tart.hideturtle()
    tart.width(2)
    tart.circle(razao)

def desenha_ponteiroh(tart):
    tart.hideturtle()
    tart.up()
    tart.left(90)
    tart.forward(razao)
    tart.down()
    tart.width(7)
    tart.left(45)
    tart.forward(razao/2)

def desenha_ponteirom(tart):
    tart.hideturtle()
    tart.up()
    tart.left(90)
    tart.forward(razao)
    tart.down()
    tart.width(5)
    tart.right(120)
    tart.forward(razao/1.5)

def desenha_ponteiros(tart):
    tart.hideturtle()
    tart.up()
    tart.left(90)
    tart.forward(razao)
    tart.down()
    tart.width(3)
    tart.color("red")
    tart.right(100)
    tart.forward(razao/1.1)

def desenha_marcadores(tart):
    tart.hideturtle()
    tart.pensize(3)
    tart.left(90)
    tart.up()
    tart.forward(razao*0.1)
    tart.right(90)
    tart.down()
    for i in range(12):
        tart.penup()
        tart.circle(razao*0.9, 360/12)
        tart.pendown()
        tart.dot()
   
    
    
    
    
desenha_borda(construtorBorda)
desenha_ponteiroh(construtorPonteiroH)
desenha_ponteirom(construtorPonteiroM)
desenha_ponteiros(construtorPonteiroS)
desenha_marcadores(construtorMarcadores)  
