# 配列 A の要素数 N と整数 K, 配列 A の各要素 A_1, A_2, ..., A_N が与えられるので、配列 A に K がいくつ含まれるか数えてください。



n, k = map(int,input().split())

count = 0
for _ in range(n):
    num = int(input())
    if num == k:
        count += 1
print(count)


# 解答2
n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
ans = 0

for i in a:
    if i == k:
        ans += 1

print(ans)