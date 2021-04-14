# N 個の 0 以上 9 以下の整数が与えられます。各数値の出現回数をそれぞれ求め、「0」の出現回数、「1」の出現回数、...「9」の出現回数、と順に数値を半角スペース区切りで出力してください。

n = int(input())
numbers = list(map(int,input().split()))

ans = [0,0,0,0,0,0,0,0,0,0,]
for n in numbers:
    ans[n] += 1

numbers_to_s = list(map(str,ans))
ans = " ".join(numbers_to_s)
print(ans)