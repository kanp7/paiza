# N 個の文字列が入った、配列Sが与えられます。各 1 ≦ i ≦ Q に対して、以下の質問に答えてください。
# * 文字列T_iが与えられます。S_j == T_i となる最も小さな j を出力してください。ただし、Sの中にT_iがない場合は -1 を出力してください。

n, q = map(int,input().split())
# 3 2

l = []
for _ in range(n):
    l.append(input())
# ['a', 'b', 'c']

l2 = []
for _ in range(q):
    l2.append(input())
# ['b', 'd']

for n in l2:
    if n in l:
        print(l.index(n)+1)
    else:
        print(-1)

# 下記のように関数にしてもOK
def my_index(l, x, default=False):
    return l.index(x)+1 if x in l else default

for n in l2:
    print(my_index(l,n,-1))
