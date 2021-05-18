# スペースで区切られた英単語列が与えられます。
# 英単語列に含まれる英単語の出現回数を出現した順番に出力してください。

li = input().split()
dic = {}
for l in li:
    dic[l] = li.count(l)

for key, value in dic.items():
    print(key,value)