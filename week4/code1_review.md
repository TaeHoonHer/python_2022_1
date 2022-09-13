## week4_code

<br></br>

### turtle이란?
- 파이썬에서 사용하는 그래픽 모듈
  - 실행환경
    - Idle, Vscode, trinket 등 에서 사용 가능
  
  - turtle 라이브러리 명령어
  ```python
  import turtle
  ```
  
## 4주차 문제

`별 그리기`
- turtle을 사용하여 별을 그려라, 다만 별 안에 있는 오각형은 선의 색을 `red`로 설정하여 그려보도록 해라

```python
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
```

> `mytri`라는 함수를 하나 생성 후, 해당 함수 안에 별을 그리는 코드를 작성하였다
>> - 선의 색을 2개로 나눠야하기 때문에, `first`와 `second`라는 2개의 변수를 생성해준다
>> - 오각형의 선, 오각형이 아닌 선을 나누면 5:3:5다
>> - pencolor을 통해 색을 정해주고, forward를 통해 turtle을 이동시킨다
>> - 별을 그림에 있어 각도를 정해주어야 하기 때문에, `left(144)`를 통해 각도를 정해준다
>> 
