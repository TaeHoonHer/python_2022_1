## 문제
lt2 = [(3,4),(5,6),(7,8)] 를 입력받고,  출력형태가  [7,11,15] 이 되도록 프로그램 하시오.
- 단, 함수 2개 이상 만들어서 문제를 해결 하세요.

<br></br>

### 함수란?
- 특정 작업을 수행하는 코드를 묶은 후 이름을 붙인 것

### 예시
```python
def Myadd2(x_tu):
  return x_tu[0] + x_tu[1]
```
#### 위 함수 해설
- Myadd2라는 함수를 만든 후, 뒤에 x_tu라는 매개변수를 통해 값을 받아온다
- 그 후, x_tu로 들어오는 값에 [0], [1] 번째 인덱스를 더해 return한다

<br></br>

``` python
def Myadd4(x_lt):
  lt = []
  for kk in x_lt:
    lt.append(Myadd2(kk))
  return lt
```
#### 위 함수 해설
- lt라는 배열을 하나 생성
- for문을 통해 매개변수 x_lt안에 들어오는 값 만큼 반복한다
- .append를 통해 배열 lt에 x_lt를 거쳐 들어오는 kk 값을 하나씩 Myadd 함수에 넣는다
- Myadd에서 더해진 후 나온 결과 값들은 배열 lt에 저장이 되어있으니
- 해당 값들을 return한다
