# パイザ君と霧島京子は最初どちらも数 1 をもっています。パイザ君は自分の番が来ると、自分のもっている数の a 倍を霧島京子の数に足してあげます。霧島京子は自分の番が来ると、自分のもっている数を b で割った余りをパイザ君の数に足してあげます。この手続きをパイザ君の番から始めて、霧島京子の数がnより大きくなるまで繰り返します。

# 手続きが終わったときのパイザ君の操作回数を求めてください。

# 失敗
n = int(input())
a,b = list(map(int,input().split()))

paiza = 1
kyoko = 1
count = 0

while kyoko < n:
    kyoko += paiza*a
    count += 1
    if kyoko > n:
        break
    paiza += kyoko%b
print(count)


# 解答
n = int(input())
[a, b] = input().split()
a, b = int(a), int(b)
paiza = 1
kyoko = 1

times = 0

while True:
    times += 1
    kyoko += paiza * a

    if kyoko > n:
        break

    paiza += kyoko % b

print(times)