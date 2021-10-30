# 整数 N が与えられます。
# N の約数の個数を出力してください。
# 約数とは、N を割り切る整数のことを指します。


n = int(input())
count = 0
for i in range(1,n+1):
    if n % i == 0:
        count += 1
print(count)
        