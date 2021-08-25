# 整数 N が与えられるので、2 以上 N 以下の素数の個数を求めてください。
# 素数とはの約数が 1 と X のみであるような整数 X のことを指します。


n = int(input())
ans = 0
for i in range(1,n+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        ans += 1
print(ans)


# 解答2
n = int(input())

ans = 0
for i in range(2, n + 1):
    is_prime = True
    for j in range(2, int(i ** (1 / 2)) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        ans += 1

print(ans)

# 素数の定義は、「 1 とその数以外の約数を持たないような数」 です。
# よって、ループを用いて 2 〜 N の数のうち、この条件が成り立つ数がいくつあるかを調べれば良いです。
# ある数 X について、素数であるかどうかを調べるには、2 〜 X の 0.5 乗（ルート N ）の全ての数で割り切れないことを確認できればよいです。
# 証明は以下の通りです。

# X の 約数候補の整数 x (1 ≦ x ≦ X) を考えると、y = X / x が整数であるならば x は約数であり、このとき x = X / y も整数となり y も約数となる。
# よって、X の約数のうち大きいほうから i 番目の約数 D_i と小さいほうから i 番目の約数 d_i に関して d_i × D_i = X が成り立ちます。
# つまり X の約数のうち小さいほうのみを考えれば良いので 2 ~ X の 0.5 乗（ルート N ）で X を割り切れるかを調べることで X が素数かどうかを調べることができます。
# X = 81 を例にとって考えます。X の約数は次の通りです。
# 1 3 9 27 81 約数を列挙したときの中央値は N の 0.5 乗（ルート N ）である 9 となっています。
# 2 〜 N のループと、素数判定のループの二重ループを実装することでこの問題を解くことができます。
