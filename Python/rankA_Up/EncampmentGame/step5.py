# 盤面の情報とマスを '?' にする距離の個数 N, マスを '?' にするときの距離 l_i が与えられます。

# 現在プレイヤーのいるマスは '*' になっており、そのマスはプレイヤーの陣地です。

# プレイヤーは次の操作をできなくなるまで続けます。

# ・ 現在の陣地から 1 マス移動することで到達できるマスをプレイヤーの陣地にして、'*' にする。
# ただし、障害物( '#' )のマスは陣地にできない。また、プレイヤーの開始時の位置からの距離が l_i であるとき、'*' の代わりに '?' にする。

# なお、はじめにプレイヤーのいるマスの開始時の位置からの距離は 0 とします。



# このコードでは paint をキューとして使います。
# まず最初に ? にするべき距離を question に入れます。
# 次に * の座標と距離を paint に追加します。
# paint から座標と距離を取り出し、上下左右に移動出来るか確認します。
# このとき距離が question に入っているようならマスを ? に書き換え、そうでないなら * に書き換えます。
# この処理を paint の中身が空になるまでループします。

H, W, n = map(int, input().split())
s = [list(input()) for _ in range(H)]
question = [int(input()) for _ in range(n)]
paint = []

for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            if 0 in question:
                s[y][x] = "?"
            paint.append([y, x, 1])

while len(paint) > 0:
    [y, x, n] = paint[0]
    paint.pop(0)
    ast_or_que = "*"
    if n in question:
        ast_or_que = "?"

    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = ast_or_que
        paint.append([y - 1, x, n + 1])
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = ast_or_que
        paint.append([y + 1, x, n + 1])
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = ast_or_que
        paint.append([y, x - 1, n + 1])
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = ast_or_que
        paint.append([y, x + 1, n + 1])

for y in range(int(H)):
    for x in range(int(W)):
        print(s[y][x], end="")
    print()
