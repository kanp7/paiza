# N 個の要素からなる数列Aが与えられます。A に対し、次の 3 つの操作をおこなうプログラムを作成してください。
# * push_back : Aの末尾にxを追加する
# * pop_back : Aの末尾を削除する
# * print : 数列Aを半角スペース区切りで出力する

n, q = map(int,input().split())

lists = list(map(int,input().split()))

for i in range(q):
    query = list(map(int,input().split()))
    if 0 in query:
        lists.append(query[1])
    elif 1 in query:
        lists.pop()
    elif 2 in query:
        print(' '.join(map(str,lists)))
        