import turtle

x = 20

huguinho = turtle.Turtle()
huguinho.shape("turtle")
huguinho.width(5)
huguinho.color("Blue")
huguinho.up()
huguinho.forward(x * 10)
huguinho.down()

zezinho = turtle.Turtle()
zezinho.shape("turtle")
zezinho.width(5)
zezinho.color("Red")
zezinho.up()
zezinho.forward(x * 5)
zezinho.down()

luizinho = turtle.Turtle()
luizinho.shape("turtle")
luizinho.width(5)
luizinho.color("Green")

for i in range(24):
    huguinho.right(15)
    huguinho.forward(x)
    zezinho.right(15)
    zezinho.forward(x)
    luizinho.right(15)
    luizinho.forward(x)
