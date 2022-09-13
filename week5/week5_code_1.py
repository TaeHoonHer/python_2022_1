import turtle
aaa = turtle.Turtle()


def MyPloygon4(x_pos):
  left = x_pos[0][0]
  top = x_pos[0][1]
  right = x_pos[1][0]
  down = x_pos[1][1] 
  
  aaa.penup()
  aaa.goto(left,top)
  
  aaa.pendown()
  aaa.goto(right,top)
  aaa.right(90)
  aaa.goto(right,down)
  aaa.right(90)
  aaa.goto(left,down)
  aaa.right(90)
  aaa.goto(left,top)
  aaa.right(90)
  
MyPloygon4([(-100,100),(100,-100)])
MyPloygon4([(-150,50),(150,-50)])
