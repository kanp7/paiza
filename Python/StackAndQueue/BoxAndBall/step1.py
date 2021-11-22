# Q 個のクエリが与えられます。 2 つのキューを用意したあと、 Q 個のクエリを順に処理してください。各クエリは、以下の 5 つのいずれかです。

# ・ PUSH 1 X: 1 つ目のキューに数値 X を追加
# ・ PUSH 2 X: 2 つ目のキューに数値 X を追加
# ・ POP 1: 1 つ目のキューの先頭の要素を削除し、その値を出力
# ・ POP 2: 2 つ目のキューの先頭の要素を削除し、その値を出力
# ・ SIZE: 1 つ目のキュー、 2 つ目のキューに含まれる要素数をそれぞれ出力

n = int(input())
queue1 = []
queue2 = []

for _ in range(n):
    query = input().split()
    if query[0] == '1':
        if query[1] == '1':
            queue1.append(query[2])
        else:
            queue2.append(query[2])
    elif query[0] == '2':
        if query[1] == '1':
            print(queue1.pop(0))
        elif query[1] == '2':
            print(queue2.pop(0))
    else:
        print(len(queue1), len(queue2))