import turtle
aaa = turtle.Turtle()
bbb = turtle.Turtle()

aaa.pencolor('red')
bbb.pencolor('blue')

a = 5

for kk in range(a):
    for kk in range(100):
        aaa.forward(1)
        bbb.forward(1)
    
    aaa.left(360/a)
    bbb.right(360/a)

turtle.done()
