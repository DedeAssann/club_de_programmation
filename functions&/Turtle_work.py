
import turtle

carre = turtle.Turtle()

for i in range(4):
    carre.fd(200)
    carre.left(90)

turtle.done()

star = turtle.Turtle()

while True:
   star.fd(200)
   star.left(150)
   if star.pos() == star.position():
    break
turtle.done()
