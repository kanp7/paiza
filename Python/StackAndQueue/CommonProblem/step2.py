# Q 個のクエリが与えられます。空の配列 A を用意したあと、 Q 個のクエリを順に処理してください。各クエリは、以下の 2 つのいずれかです。

# ・ PUSH X: 配列 A の末尾に X を追加
# ・ STAY: 何もしない

# すべてのクエリの処理が終わったあと、配列 A の要素数 N と値をそれぞれ改行区切りで出力してください。

query_num = int(input())
array = []

for _ in range(query_num):
    query = list(map(int,input().split()))
    if query[0] == 2:
        pass
    else:
        array.append(query[1])

print(len(array))
for n in array:
    print(n)
    
    