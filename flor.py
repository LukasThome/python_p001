import turtle

construtor = turtle.Turtle()
razao = 150
def desenha_petala(tart):
    tart.hideturtle()
    tart.up()
    tart.circle(razao, extent = 45)
    tart.down()
    tart.circle(razao, extent = 225)
    tart.circle(razao)
desenha_petala(construtor)