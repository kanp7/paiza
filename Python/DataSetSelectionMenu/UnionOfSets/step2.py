# N 個の要素からなる数列Aが与えられます。数列Aは昇順にソートされています。Aの重複した要素を取り除いて昇順に出力してください。

n = int(input())
numbers = set(map(int,input().split())) #setにして重複を削除、intにすることで順序が整う
numbers = list(map(str,numbers)) #結合時の都合により、一度文字列に戻してリスト化
print(" ".join(numbers))