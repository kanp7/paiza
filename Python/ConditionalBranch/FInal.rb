# 長さ N の数列Aが与えられます。Aの中に 0 が含まれていない場合はYESを、 0 が含まれている場合はNOを出力してください。

n = int(input())

lists = []
for _ in range(n):
    i = int(input())
    lists.append(i)

if 0 in lists:
    print("NO")
else:
    print("YES")