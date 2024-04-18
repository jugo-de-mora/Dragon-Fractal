import turtle
import random

def sierpinski(depth,x,y,length,col):
   if depth == 0:
      return
   # 1
   go(x,y)
   t.up()
   t.setheading(0)
   t.lt(60)
   t.fd(length/4)
   pos_1 = t.pos()

   # 2
   t.setheading(180)
   t.lt(60)
   t.fd(length/2)
   pos_2 = t.pos()

   # 3
   go(x,y)
   t.setheading(0)
   t.fd(length/2)
   # t.setheading(180)
   t.lt(240)
   t.fd(length/4)
   pos_3 = t.pos()
   t.down()

   t.fillcolor(get_color(col))
   t.begin_fill()
   go(x,y)
   t.setheading(0)
   t.fd(length/2)
   t.lt(240)
   t.fd(length/2)
   t.rt(120)
   t.fd(length/2)
   t.end_fill()
   sierpinski(depth - 1, pos_1[0], pos_1[1], length / 2, col + 1)
   sierpinski(depth - 1, pos_2[0], pos_2[1], length / 2, col + 1)
   sierpinski(depth - 1, pos_3[0], pos_3[1], length / 2, col + 1)

def get_color(n):
   colors = ['#F5F0BB', '#C4DFAA', '#90C8AC', '#73A9AD', '#8DDC96']
   return colors[n % 5]

def triangle():
   t.fillcolor('BlanchedAlmond')
   t.begin_fill()
   t.fd(580)
   t.lt(120)
   t.fd(580)
   temp = t.pos()
   t.lt(120)
   t.up()
   t.fd(580/2)
   pos_mid = t.pos()
   t.down()
   go(temp[0],temp[1])
   t.fd(580)
   t.end_fill()
   return pos_mid

def go(x,y):
   t.up()
   t.goto(x,y)
   t.down()
   
turtle.Screen().bgcolor('black')
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
go(-300,-300)
pos = triangle()
sierpinski(7,pos[0],pos[1],580,0)
turtle.exitonclick()
