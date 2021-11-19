# Q 個のクエリが与えられます。空の配列 A を用意したあと、 Q 個のクエリに応じて以下の 2 種類の処理をしてください。

# ・ PUSH X: 配列 A の末尾に 文字 X を追加
# ・ POP: 配列 A の末尾にある要素を出力し、削除

# 各クエリの処理が終わったあと、配列 A の各要素の値を半角スペース区切りで出力してください。

n = int(input())
stack = []
for _ in range(n):
    query = input().split()
    if query[0] == '1':
        stack.append(query[1])
    elif query[0] == '2':
        poped = stack.pop()
        print(poped)
    print(" ".join(stack))