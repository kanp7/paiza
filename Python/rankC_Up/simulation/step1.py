# 10000 以上かつ 13 で割り切れるような最小の自然数を求めてください。


n = 10000
while True:
    if n % 13 == 0:
        break
    n += 1
print(n)