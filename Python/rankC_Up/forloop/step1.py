# 正整数 n と、 n 個の整数 a_1, ..., a_n が半角スペース区切りで与えられます。
# 与えられた整数の中に 3 の倍数がいくつあるかを数え、出力してください。


n = int(input())
nums = list(map(int,input().split()))
ans = 0

for n in nums:
    if n % 3 == 0:
        ans += 1
print(ans)