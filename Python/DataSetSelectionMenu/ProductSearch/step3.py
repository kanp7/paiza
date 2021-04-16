# 文字列がN個与えられます。各文字列の出現回数を文字列の辞書順で出力してください。

n = int(input())

array = []
for _ in range(n):
    string = input()
    array.append(string)

dic = {}
for s in array:
    dic[s] = (array.count(s))


dic_sorted = sorted(dic.items(), key=lambda x:x[0])

for key, value in dic_sorted:
    print(key,value)

