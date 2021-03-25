# 2つの整数の組がn個与えられるので、各組の計算結果を足し合わせたものを出力してください。
# 各組の計算結果は次の値です。
# ・2つの整数の組を足し合わせたもの
# ・ただし、2つの整数が同じ値だった場合は、掛け合わせたもの

n = int(input())

sum = 0
for _ in range(n):
    a,b = map(int,input().split())
    if a == b:
        sum += a*b
    else:
        sum += a + b
print(sum)