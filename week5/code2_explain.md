## 문제2
`goto() 를 이용해서 3개 이상의 튜플 좌표값을 받는 MyPloygon() 함수를 작성해보자.`
>- 첫번째 좌표 이동은 enumerate 를 사용한다.
>- 호출 예 : MyPloygon((-100,100),(100,100),(-100,-100),(-100,100))  #좌표4개인경우
>- 호출 예 : MyPloygon((-100,100),(100,100),(100,-100),(-100,-100),(-100,100)) #좌표5개인경우

``` python
import turtle
aaa = turtle.Turtle()

def mypoly(*args):
    for ii, kk in enumerate(args):
        if ii == 0:
            aaa.penup()
        else:
            aaa.pendown()
        aaa.goto(kk[0], kk[1])
```

>- `turtle` import
>>- mypoly라는 함수 생성
>>- enumerate를 통해 kk로 들어가는 args값들의 번호를 ii에다가 넣는다
>>- ii가 0이면 penup
>>- 그게 아니면 pendown
>>- goto문을 통해 원하는 지점으로 이동한다
