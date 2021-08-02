# m 本の相異なる長さ n の数列 A_1, A_2, ..., A_m と、長さ n の数列 X が与えられます。
# 数列 X が A の何本目の数列と等しいかを求めてください。つまり、X_1 = A_i_1, X_2 = A_i_2, ..., X_n = A_i_n を満たす整数 i を求めてください。
# なお、数列 X は必ずある A_i と等しいことが保証されます。


m, n = map(int,input().split())

nums = []
for _ in range(m):
    nums.append([int(x) for x in input().split()])
# print(nums) [[8, 1, 3, 8], [1, 3, 8, 1], [1, 1, 1, 1]]

x = list(map(int,input().split()))
# print(x)[1, 3, 8, 1]

for i, row in enumerate(nums):
    if row == x:
        print(i+1)


# 解答2
m, n = map(int, input().split())
a = []
for i in range(m):
    a.append([int(t) for t in input().split()])
x = [int(t) for t in input().split()]

pos_of_x = 0
for i in range(m):
    is_x = True
    for j in range(n):
        if a[i][j] != x[j]:
            is_x = False

    if is_x:
        pos_of_x = i + 1
        break

print(pos_of_x)