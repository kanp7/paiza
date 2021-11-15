# N 個の整数 a_1, a_2, ..., a_N が与えられます。
# a_i に i を足したとき、a_1 , ... , a_N の最大値を出力してください。

n = int(input())
nums = list(map(int,input().split()))

ans = 0
i = 1
for num in nums:
    if num + i > ans:
        ans = num + i
    i += 1


print(ans)