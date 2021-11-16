# 10 進数で表された整数 N が与えられます。
# 整数 N の各桁の和を計算し、出力してください。

nums = list(input())
ans = 0

for n in nums:
    ans += int(n)
print(ans)