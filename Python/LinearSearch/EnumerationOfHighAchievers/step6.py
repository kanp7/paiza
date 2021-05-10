# 整数 n と、二次元平面上の点 1 ~ n の座標 (x_1, y_1), ... , (x_n, y_n), 整数 x_s, x_t, y_s, y_t が与えられます。

# n 個の点のうち、(x_s, y_s), (x_s, y_t), (x_t, y_t), (x_t, y_s) の4頂点からなる長方形の内部に含まれている点の数を求めてください。なお、長方形の辺上にある点は長方形に含まれているものとします。
n = int(input())

l = []
for _ in range(n):
    x,y = list(map(int,input().split()))
    l.append([x,y])
x_s, x_t = list(map(int,input().split()))
y_s, y_t = list(map(int,input().split()))

ans = []
for n in l:
    if (n[0] >= x_s and n[0] <= x_t) and (n[1] >= y_s and n[1] <= y_t):
        ans.append(n)
print(len(ans))