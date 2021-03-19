# 長さ N の数列Aが与えられます。この数列に含まれる偶数の要素の個数と、奇数の要素の個数を答えてください。

n  = int(input())
numbers = map(int,input().split())

odd = 0
even = 0

for i in numbers:
    if (i+1) % 2 == 0:
        even += 1
    else:
        odd += 1

print(odd,even)
