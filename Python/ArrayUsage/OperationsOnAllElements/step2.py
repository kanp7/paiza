# 配列 A の要素数 N と配列 A の各要素 A_1, A_2, ..., A_N が整数として与えられるので、配列 A の全ての要素の和を求めてください。


n = int(input())
total = 0
for _ in range(n):
    n = int(input())
    total += n
print(total)


# 解答2
n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    ans += i

print(ans)

# 解答3
n = int(input())
a = [int(input()) for _ in range(n)]

ans = sum(a)

print(ans)
