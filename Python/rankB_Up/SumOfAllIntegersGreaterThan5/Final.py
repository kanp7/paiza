# 改行区切りで整数がn個入力されるので、n個の整数のうち、5以上のものをすべて足し合わせた値を出力してください。

n = int(input())

sum = 0
for _ in range(n):
    i = int(input())
    if i >= 5:
        sum += i
print(sum)