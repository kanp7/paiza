# へびがマップ上を移動していきます。
# マップの行数 H と列数 W , 障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy , sx , 方向転換の回数 N が与えられます。
# 続けて N 回の方向転換する時刻 t_1 ... t_N , 転換する向き d_1 ... d_N が与えられます。

# へびははじめ、北を向いています。

# 時刻 0 から 99 までの間、へびは各時刻に次の行動を最大 100 回とります。

# ・ 方向転換をおこなう時刻の場合、指定の向きに方向転換したのち 1 マス身体を伸ばす。
# ・ そうでない時は移動が可能な場合に限り、今向いている方向に 1 マス身体を伸ばす。

# 各移動が可能であるということは、
# 「移動先のマスに障害物がない かつ 移動先がマップの範囲外でない」
# ということを意味します。

# 各移動が可能である場合、各移動が終了した時の y , x 座標を出力してください。
# 移動が可能でない場合、"Stop" を出力して以降の移動を打ち切ってください。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

# 移動の一例をあげます。例えば次のような入力が与えられた時は図のような移動になります。



h, w, sy, sx, n = input().split()
s = [list(input()) for _ in range(int(h))]
time_lr = [input().split() for _ in range(int(n))]
sy = int(sy)
sx = int(sx)
directions = ["N", "E", "S", "W"]
now_direction = 0
time_index = 0

for t_now in range(100):
    if str(t_now) == time_lr[time_index][0]:
        d = time_lr[time_index][1]
        time_index += 1
        if d == "L":
            now_direction = (3 + now_direction) % 4
        else:
            now_direction = (1 + now_direction) % 4

    if directions[now_direction] == "N":
        sy -= 1
    elif directions[now_direction] == "E":
        sx += 1
    elif directions[now_direction] == "S":
        sy += 1
    elif directions[now_direction] == "W":
        sx -= 1

    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] == "#":
        print("Stop")
        break
    else:
        print(sy, sx)