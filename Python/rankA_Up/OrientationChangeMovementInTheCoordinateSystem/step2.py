# 開始時点の y , x 座標 と移動の回数 N が与えられます。
# 続く N 行で移動の方角 d_1 ... d_N が与えられるので、与えられた順に移動をしたときの各移動後の y , x 座標 を答えてください。

# ただし、図の通り、上側（ y 軸の負の向き）を北とします。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


y, x ,n = map(int,input().split())

for _ in range(n):
    direction = input()
    if direction == "N":
        y -= 1
    elif direction == "S":
        y += 1
    elif direction == "W":
        x -= 1
    elif direction == "E":
        x += 1
    print(y, x)
