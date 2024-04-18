import turtle
import time

def dragon(depth,pos_ang,length):
   if depth == 0:
      return
   time.sleep(0)
   t.clear()
   array = []
   length *= 0.707
   counter = 1
   for x,y,a in pos_ang:
      go(x,y)
      t.setheading(a)
      even = counter % 2 == 0
      if even:
         t.rt(45)
      else:
         t.lt(45)
      new_pos = t.pos()
      new_ang = t.heading()
      array.append([new_pos[0],new_pos[1],new_ang])
      t.fd(length)
      if even:
         t.lt(90)
      else:
         t.rt(90)
      new_pos = t.pos()
      new_ang = t.heading()
      array.append([new_pos[0],new_pos[1],new_ang])
      t.fd(length)
      counter += 1
   dragon(depth-1,array,length)

def initial():
   go(-300,-100)
   pos = t.pos()
   ang = t.heading()
   t.fd(580)
   return [pos[0],pos[1],ang]
   
def go(x,y):
   t.up()
   t.goto(x,y)
   t.down()

t = turtle.Turtle()
t.speed(0)
t.ht()
t.color('white')
turtle.Screen().bgcolor('black')
pos_ang = [initial()]
dragon(8,pos_ang,580)
turtle.exitonclick()