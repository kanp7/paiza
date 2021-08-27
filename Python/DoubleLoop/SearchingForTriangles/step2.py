# 配列 A の要素数 N とその要素 A_i (1 ≦ i ≦ N) が与えられるので、A についてのかけ算表 B を出力してください。かけ算表は N * N の二次元配列の形式とし、B の i 行 j 列の要素 B_ij について、B_ij = Ai * Aj (1 ≦ i , j ≦ N) が成り立つものとします。

# 例として、A = [1,2,3] のとき B は


# 1 2 3
# 2 4 6
# 3 6 9


# となります。


n = input()
nums = list(map(int,input().split()))
for i in nums:
    tmp = []
    for j in nums:
        tmp.append(i*j)
    print(*tmp)


# 解答2
n = int(input())
a = [int(i) for i in input().split()]
b = [[None] * n] * n

for i in range(n):
    for j in range(n):
        b[i][j] = a[i] * a[j]

for i in range(n):
    for j in range(n):
        if j == n - 1:
            print(b[i][j])
        else:
            print(b[i][j], end=" ")