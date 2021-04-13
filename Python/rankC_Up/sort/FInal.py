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