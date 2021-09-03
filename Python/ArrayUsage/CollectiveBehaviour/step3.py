# データ構造の queue と同様の働きをするロボットがあります。ロボットは指示に応じて配列 A に対して 2 種類の仕事を行います、仕事の内容は以下の通りです。

# ・in n と指示された場合、A の末尾に n を追加してください。
# ・out と指示された場合、A の先頭の要素を削除してください。ただし、A が既に空の場合、何も行わないでください。


# ロボットに与えられる指示の回数 N と、各指示の内容 S_i が与えられるので、ロボットが全ての処理を順に行った後の A の各要素を出力してください。
# なお、初め配列 A は空であるものとします。

n = int(input())
array = []

for _ in range(n):
    order = input().split()
    if len(order) >= 2:
        array.append(order[1])
    else:
        if len(array) >= 1:
            array.pop(0)

for n in array:
    print(n)


# 解答

# ここでは リストを queue として扱います。
# ループを使い入力を空白区切りで受け取ります。
# 受け取った値の 1 つ目が "in" なら受け取った値の 2 つ目を queue に追加します。
# 受け取った値の 1 つ目が "out" で queue に要素があるなら先頭の値を削除します。

n = int(input())
queue = []
for i in range(n):
    s_i = input().split()
    if s_i[0] == "in":
        queue.append(s_i[1])
    elif s_i[0] == "out" and len(queue) > 0:
        queue.pop(0)

for i in queue:
    print(i)
