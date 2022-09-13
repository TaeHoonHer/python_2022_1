import turtle

aaa = turtle.Turtle()

def mytri(x):
    first = x * 5 / 13
    second = x * 3 /13
    for kk in range(5):
        aaa.pencolor('black')
        aaa.forward(first)
        aaa.pencolor('red')
        aaa.forward(second)
        aaa.pencolor('black')
        aaa.forward(first)
        
        aaa.left(144)
        
mytri(200)
