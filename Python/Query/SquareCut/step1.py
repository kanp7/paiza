# 長さ N の数列 A と、K 個の整数 Q_1 ... Q_K が与えられるので、各整数 Q_i (1 ≦ i ≦ K) について A_1 ... A_{Q_i} の和を求めてください。

n, k = list(map(int,input().split()))

add_nums = []
sums = 0
for _ in range(n):
    num = int(input())
    sums += num
    add_nums.append(sums)

for _ in range(k):
    q = int(input())
    print(add_nums[q-1])