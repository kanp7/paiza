# 開始時点の x , y 座標、移動の回数 N が与えられます。
# 続くN行で移動の向き d1 ... dN が与えられるので、与えられた順に移動をしたときの各移動後の x , y 座標 を答えてください。
# 移動者ははじめ北を向いています。

# なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

# ・ 移動をするごとに向く方角が変わること
# ・ 移動前に向いている方角によって同じ移動の向きでも座標の変化が違うこと
# の 2 点に気をつけてください。
# 例えば、上の図の状態から右に移動を行った場合、下の図のような状態になります。


x, y, n = map(int, input().split())
directions = ["N", "E", "S", "W"]
now_direction = 0

for _ in range(n):
    lr = input()
    if lr == "L":
        now_direction = (3 + now_direction) % 4
    else:
        now_direction = (1 + now_direction) % 4

    if directions[now_direction] == "N":
        y -= 1
    elif directions[now_direction] == "E":
        x += 1
    elif directions[now_direction] == "S":
        y += 1
    elif directions[now_direction] == "W":
        x -= 1

    print(x, y)