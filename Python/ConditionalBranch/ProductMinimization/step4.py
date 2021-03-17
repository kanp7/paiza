# 長さ N の数列Aが与えられます。 1 つ目の要素から最も左にある奇数の要素の手前までの値の和を求めてください。
# 形式的には、A_iが奇数かつ、区間 [A_1, A_{i - 1}] がすべて偶数であるとき、\sum_{j=1}^{i-1}{A_j}を求めてください。

n = int(input())

num = 0

numbers = map(int,input().split())

for n in numbers:
    if n % 2 == 0 :
        num += n
    else:
        break
print(num)


