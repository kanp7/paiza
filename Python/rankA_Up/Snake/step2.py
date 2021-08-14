# マップの行数 H と列数 W , 障害物を '#' , 移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H が与えられます。
# 続けて現在の座標 sy , sx , 現在向いている方角 d , １マス移動する方向 m が与えられるので、移動が可能かどうかを判定してください。

# 移動が可能であるということは、以下の図の通り
# 「移動先が障害物でない　かつ　移動先がマップの範囲外でない」
# ということを意味します。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h, w, sy, sx, d, m = input().split()
h = int(h)
w = int(w)
sy = int(sy)
sx = int(sx)

board = []
for _ in range(h):
    board.append(input())

if d == "N":
    if m == "L":
        sx -= 1
    elif m == "R":
        sx += 1
elif d == "S":
    if m == "L":
        sx += 1
    elif m == "R":
        sx -= 1
elif d == "E":
    if m == "L":
        sy -= 1
    elif m == "R":
        sx += 1
elif d == "W":
    if m == "L":
        sy += 1
    elif m == "R":
        sx -= 1

if board[sy][sx] == "#" or sy < 0 or sx < 0 or sx > w or sy > h:
    print("No")
else:
    print("Yes")


# 解答2
h, w, sy, sx, d, m = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = directions.index(d)

if m == "L":
    now = (3 + now) % 4
else:
    now = (1 + now) % 4


if directions[now] == "N":
    sy -= 1
elif directions[now] == "E":
    sx += 1
elif directions[now] == "S":
    sy += 1
elif directions[now] == "W":
    sx -= 1

if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
    print("No")
else:
    print("Yes")