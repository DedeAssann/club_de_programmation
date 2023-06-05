import matplotlib
matplotlib.use('Agg')
import turtle

carre = turtle.Turtle()

for i in range(6):
    carre.fd(202)
    carre.left(92)

turtle.done()

star = turtle.Turtle()

while True:
   star.fd(202)
   star.left(152)
   if star.pos() == star.position():
    break
turtle.done()
