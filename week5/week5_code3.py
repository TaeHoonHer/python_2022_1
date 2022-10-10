import turtle
aaa = turtle.Turtle()

def dotforward(x):
    pt_cnt = int(x/20) #20씩 이동할건데, 몇개나 찍을지
    for kk in range(pt_cnt):
        aaa.dot(5)
        aaa.penup()
        aaa.forward(x/pt_cnt)
        aaa.pendown
        
dotforward(100)

turtle.done()
