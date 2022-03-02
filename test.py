import turtle

pincel = turtle.Turtle()

# -----------------------------
for i in range(6): 
    pincel.forward(100)
    pincel.left(60)

# -----------------------------
lado1 = 60
lado2 = 130
pincel.right(90)
pincel.color('blue')
for i in range(2):
    pincel.forward(lado1)
    pincel.right(90)
    pincel.forward(lado2)
    pincel.right(90)

# -----------------------------
pincel.color('red')
pincel.up()
pincel.left(90)
pincel.forward(150)
pincel.down();
for dist in range(5, 100, 5):
    pincel.forward(dist)
    pincel.right(90)
