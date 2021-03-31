# 1行目に行数を表す整数 n、続く n 行の各行で「文字」と「整数」の組が空白区切りで入力されます。
# n 個の組について、「文字」の値が同じ組同士の数値を足しわせてまとめ、まとめた数値の降順で、文字とまとめた数値の組を出力してください。

n = int(input())

dic = {}
for  _ in range(n):
    s, d = input().split()
    d = int(d)
    if s in dic.keys():
        d = dic[s] + d
        dic[s] = d
    else:
        dic[s] = d

sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse = True)

for key, value in sorted_dic:
    print(key,value)
