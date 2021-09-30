# 整数 n が与えられるので、n 回、半角スペース区切りで paiza と出力してください。


n = int(input())
s = ''
for _ in range(n):
    s += "paiza "
print(s.strip())

# 解答2
n = int(input())

a = ["paiza"] * n

print(" ".join(a))