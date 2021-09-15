# N 人の人々がおり、それぞれの人は金と銀を何キログラムか持っています。今は金の方が銀よりも価値が高いですが、ある日金と銀の価値が逆転して、人々の財産の多さは次のように決定されるようになりました。

# 1. 持っている銀が多い方が財産が多い。
# 2. 持っている銀が同じなら、持っている金が多い方が財産が多い。

# それぞれの人が持っている金と銀のキログラム数が与えられるので、この規則にしたがって、財産を多い順に並び替えて出力してください。

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split(' '))))
# print(l)

l = sorted(l, key=lambda x: x[0], reverse=True,)
# print(l)
l = sorted(l, key=lambda x: x[1], reverse=True,)

for g, s in l:
    print(g, s)

# 失敗したコード
# n = int(input())
# dic = {}
# for _ in range(n):
#     g,s = map(int,input().split())
#     dic[g] = s
# sort_gold = sorted(dic.items(), reverse=True, key=lambda x:x[0])
# dic.clear()
# dic.update(sort_gold)

# sort_silver = sorted(dic.items(), reverse=True, key=lambda x:x[1])

# for k,v in sort_silver:
#     print(k,v)

# 解答2
# 配列（Python ではリスト）の配列をソートする場合、ソート用組み込み関数の多くは「配列の 0 番目の要素を最優先で参照してソート、0 番目が同じなら 1 番目を参照してソート、1 番目が同じなら 2 番目を……」という具合にソートしてくれます。したがって、ほとんど組み込み関数に任せればOKです。
# ただし、今回はソートにあたって参照すべき要素の優先順位が逆で、「 1 番目の要素を最優先で参照してソート、1 番目が同じなら 0 番目を参照してソート」となっています。
# これに対処するためには、あらかじめ 0 番目の要素と 1 番目の要素を逆にして入力を受け取り、ソートした後に再び 0 番目の要素と 1 番目の要素を入れ替えて出力すれば十分です。
N = int(input())
kingin = [0] * N

for i in range(N):
    [a, b] = [int(j) for j in input().split()]
    kingin[i] = [b, a]

kingin.sort(reverse=True)

for i in range(N):
    [a, b] = kingin[i]
    print(b, a)