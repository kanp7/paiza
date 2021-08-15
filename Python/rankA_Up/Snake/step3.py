# マップの行数 H と列数 W , 現在の座標 sy , sx , 移動の回数 N が与えられます。
# 続けて、障害物を '#' で、移動可能な場所を '.' で表した H 行 W 列 のマップ S_1 ... S_H と N 回の移動の向き d_1 ... d_N が与えられます。

# 移動者ははじめ北を向いています。移動者は、1 回の移動で次の行動を行います。

# 「移動の向きに方向転換したのち、1 マス進む。」

# 各移動が可能である場合、移動後の y , x 座標を出力してください。
# 移動が可能でない場合、移動後の座標を出力する代わりに "Stop" を出力して、以降の移動を打ち切ってください。

# 各移動が可能であるということは、以下の図の通り
# 「移動先が障害物でない　かつ　移動先がマップの範囲外でない」
# ということを意味します。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h,w,sy,sx,n = map(int,input().split())
directions = ["N", "E", "S", "W"]
now = 0

board = [input() for _ in range(h)]

for _ in range(n):
    lr = input()
    if lr == "L":
        if directions[now] == "N":
            sx -= 1
        elif directions[now] == "E":
            sy -= 1
        elif directions[now] == "S":
            sx += 1
        elif directions[now] == "W":
            sy += 1
        now = (3 + now) % 4
    elif lr == "R":
        if directions[now] == "N":
            sx += 1
        elif directions[now] == "E":
            sy += 1
        elif directions[now] == "S":
            sx -= 1
        elif directions[now] == "W":
            sy -= 1
        now = (1 + now) % 4
    if board[sy][sx] == "#" or sy < 0 or sx < 0 or sx > w or sy > h:
        print("Stop")
        break
    else:
        print(sy,sx)


# 解答2
h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

for _ in range(int(n)):
    d = input()
    if d == "L":
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
        print("Stop")
        break
    else:
        print(sy, sx)