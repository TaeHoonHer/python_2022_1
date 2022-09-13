import turtle
aaa = turtle.Turtle()

def mypoly(*args):
    for ii, kk in enumerate(args):
        if ii == 0:
            aaa.penup()
        else:
            aaa.pendown()
        aaa.goto(kk[0], kk[1])
        
mypoly((-100,100), (100,100), (-100,-100), (-100,100))
mypoly((-100,100), (100,100), (100,-100), (-100,-100), (-100,100))

turtle.done()
