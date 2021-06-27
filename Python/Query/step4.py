# 数列 A が与えられるので、A の先頭の要素を削除した後の A を出力してください。

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))
    
numbers.pop(0)
for n in numbers:
    print(n)
