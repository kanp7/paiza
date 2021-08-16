# マップの行数 H と列数 W , 障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy, sx, 移動の回数 N が与えられます。
# 続けて、 N 回の移動の向き d_1 ... d_N と移動するマス数 l_1 ... l_N が与えられます。

# プレイヤーははじめ北を向いています。

# 各移動が可能である場合、移動後の y , x 座標 を出力してください。
# 移動が可能でない場合(移動しきれない場合)、移動できるところまで移動した後の座標を出力した後に "Stop" を出力して、以降の移動を打ち切ってください。

# 各移動が可能であるということは、以下の図の通り
# 「今いるマスから移動先のマスまでに障害物がない　かつ　移動先がマップの範囲外でない」
# ということを意味します。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now = 0

for _ in range(int(n)):
    d_i, l_i = input().split()
    l_i = int(l_i)
    if d_i == "L":
        now = (3 + now) % 4
    else:
        now = (1 + now) % 4

    flag = False
    for i in range(l_i):
        if directions[now] == "N":
            sy -= 1
        elif directions[now] == "E":
            sx += 1
        elif directions[now] == "S":
            sy += 1
        elif directions[now] == "W":
            sx -= 1

        if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
            flag = True
            if directions[now] == "N":
                sy += 1
            elif directions[now] == "E":
                sx -= 1
            elif directions[now] == "S":
                sy -= 1
            elif directions[now] == "W":
                sx += 1
            break

    print(sy, sx)
    if flag:
        print("Stop")
        break