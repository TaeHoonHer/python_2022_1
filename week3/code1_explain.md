## code1 설명 

<br></br>

### turtle이란?
- 파이썬에서 사용할 수 있는 그래픽 모듈, turtle모양의 커서가 지나간 흔적을 바탕으로 화면에 그림을 그릴 수 있다

### 사용법
- import turtle 을 작성하여 python에 turtle을 import 시킨다

aaa = turtle.Turtle()
bbb = turtle.Turtle()
- aaa, bbb라는 변수 2개를 만들어 turtle 모듈을 해당 변수를 통해 실행시킨다

a = 5
- 변수 a에 5를 넣어 반복할 횟수를 지정한다

for kk in range(a):

- for kk in range(a)를 통해 5번을 반복하겠다 라고 for 문에 명령을 내리고

    for kk in range(100):
    
    - for문을 다시 돌려 범위를 100으로 지정한 후
    
        aaa.forward(1)
        
        - aaa.forward(1) 명령어를 입력, 1칸씩 움직이게 한다
        
        bbb.forward(1)
        
        - bbb도 마찬가지
    
    aaa.left(360/a)
    bbb.right(360/a)
    
    - 360/a를 함으로써 초반에 a를 통해 반복한 횟수만큼 360으로 나눠 원하는 다각형을 만들고. left right를 함으로써 각 각 다른 방향으로 움직이게 한다
    

turtle.done()

- turtle의 마지막은 항상 turtle.done()으로 마무리
