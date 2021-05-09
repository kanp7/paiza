# 整数 n と、二次元平面上の点 1 ~ n の座標 (x_1, y_1), ... , (x_n, y_n), 整数 k が与えられます。

# n 個の点 (点 n 含む) のうち、点 n とのマンハッタン距離が k 以下であるような点の数を求めてください。

# なお、この問題において、2点間のマンハッタン距離とは、2点の各座標の差の絶対値の総和を指します。つまり、点 (x_i, y_i) と点 (x_j, y_j) のマンハッタン距離は、| x_i - x_j | + | y_i - y_j | です。

n = int(input())
l = []
for _ in range(n):
    x, y = list(map(int,input().split()))
    temp = []
    temp.append(x)
    temp.append(y)
    l.append(temp)
k = int(input())
# [[-9, 5], [0, 4], [2, -6], [7, -4], [-3, -1]]

p_n = l[-1]

ans = []
for x,y in l:
    x_abs = abs(x - p_n[0])
    y_abs = abs(y - p_n[1])
    sum_xy = x_abs + y_abs
    if sum_xy <= k:
        ans.append(sum_xy)
print(len(ans))