lt2 = [(3,4),(5,6),(7,8)] # 출력형태 [7,11,15]

def Myadd2(x_tu):
  return x_tu[0] + x_tu[1]
  
def Myadd4(x_lt):
  lt = []
  for kk in x_lt:
    lt.append(Myadd2(kk))
  return lt


print(Myadd4(lt2))
