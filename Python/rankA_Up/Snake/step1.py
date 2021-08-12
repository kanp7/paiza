# マップの行数 H と列数 W , 障害物を '#' で、移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H が与えられます。
# 続けて現在の座標 sy , sx ,１マス移動する方角 m が与えられるので、移動が可能かどうかを判定してください。

# 移動が可能であるということは、以下の図の通り
# 「移動先が障害物でない　かつ　移動先がマップの範囲外でない」
# ということを意味します。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

h, w, sy, sx, m = input().split()
h = int(h)
w = int(w)
sy = int(sy)
sx = int(sx)
board = []
for _ in range(h):
    board.append(input())

if m == "E":
    if board[sy][sx+1] == "." and sx < w-1:
        print("Yes")
    else:
        print("No")
elif m == "W":
    if board[sy][sx-1] == "." and sx > 0:
        print("Yes")
    else:
        print("No")
elif m == "N":
    if board[sy-1][sx] == "." and sy > 0:
        print("Yes")
    else:
        print("No")
elif m == "S":
    if board[sy+1][sx] == "." and sy < h-1:
        print("Yes")
    else:
        print("No")



# 解答2
h, w, sy, sx, m = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)

if m == "N":
    sy -= 1
elif m == "E":
    sx += 1
elif m == "S":
    sy += 1
elif m == "W":
    sx -= 1

if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
    print("No")
else:
    print("Yes")