# 1行目で文字列 s、2行目で文字列 t が入力されます。
# s が t の中で何回出現するかカウントして出力してください。

s = input()
t = input()
s_length = len(s)
t_length = len(t)

count = 0
for i in range(t_length-1):
    if s == (t[:s_length]):
        count += 1
    t = t[1:]
print(count)
