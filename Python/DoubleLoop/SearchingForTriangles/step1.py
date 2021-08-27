# N 行 K 列の行列 A の i 行 j 列 の要素 A_ij を A_ji とした K 行 N 列の行列を元の配列 A の転置行列と言います。

# 例として、

# 1 2 3
# 4 5 6
# 7 8 9

# の転置行列は

# 1 4 7
# 2 5 8
# 3 6 9

# です。

# 行列 A についての情報が与えられるので、A の転置行列を出力してください。


n, k = list(map(int, input().split()))
array = [list(map(int,input().split())) for _ in range(n)]
# array = []
# for _ in range(n):
#     array.append(list(map(int, input().split())))

for i in range(k):
    tmp = []
    for row in array:
        tmp.append(row[i])
    print(*tmp)


# 解答2
n, k = map(int, input().split())
a = [input().split() for _ in range(n)]

for i in range(k):
    for j in range(n):
        if j == n - 1:
            print(a[j][i])
        else:
            print(a[j][i], end=" ")