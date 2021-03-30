# 1行目に行数を表す整数 n、続く n 行の各行で「文字」と「整数」の組が空白区切りで入力されます。
# n 個の組を、「整数」の値で昇順に並べ変え、「文字」を出力してください。

n = int(input())

dictionary = {}
for _ in range(n):
    s, d = input().split()
    d = int(d)
    dictionary[s] = d

dictionary_sorted = sorted(dictionary.items(), key=lambda x:x[1])

for key, value in dictionary_sorted:
    print(key)
