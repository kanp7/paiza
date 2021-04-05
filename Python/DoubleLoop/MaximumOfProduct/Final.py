# 配列 A と B についての情報が与えられるので、(A の 1 つの要素) × (B の 1 つの要素) の最大値を求めてください。

n, k = map(int,input().split())

numbers_a = list(map(int,input().split()))
numbers_b = list(map(int,input().split()))

ans = []
for a in numbers_a:
    for b in numbers_b:
        ans.append(a*b)

print(max(ans))