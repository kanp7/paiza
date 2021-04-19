# N 個の要素からなる数列Aと数値Bが与えられます。BがAに含まれているか判定してください。

n, b = map(int,input().split())
# 5 4
numbers = list(map(int,input().split(" ")))
# [1, 2, 3, 4, 5]

if b in numbers:
    print("Yes")
else:
    print("No")

# 三項演算子で一文で書く場合
print("Yes") if b in numbers else print("No")