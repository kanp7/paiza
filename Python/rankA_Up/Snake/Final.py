# マップ上をへびが移動していきます。
# マップの行数 H と列数 W ,障害物を '#' で移動可能な場所を '.' で表した H 行 W 列のマップ S_1 ... S_H , 現在の座標 sy , sx , 方向転換の回数 N が与えられます。
# 続けて N 回の方向転換をおこなう時刻 t_1 ... t_N, 転換する向き d_1 ... d_N が与えられます。

# へびははじめは北を向いています。

# へびは進む先のマスに自分の身体や障害物がない時に移動ができます。
# 時刻 0 から 99 までの間、へびは各時刻に次の行動を最大 100 回繰り返します。

# ・ 方向転換をおこなう時刻の場合、指定の向きに方向転換したのち １ マス身体を伸ばす。そうでない時は、今向いている方向に １ マス身体を伸ばす。

# 時刻が 99 の時の行動を終えるか、移動できなくなった時、移動を終了します。
# 移動終了時にへびの体のあるマスを '*' にしたマップを出力してください。

# 移動が可能であるということは、
# 「移動先のマスに自分の身体や障害物がない かつ 移動先がマップの範囲外でない」
# ということを意味します。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h, w, sy, sx, n = map(int, input().split())
s = [list(input()) for _ in range(int(h))]
time_lr = [input().split() for _ in range(int(n))]
directions = ["N", "E", "S", "W"]
now_direction = 0
time_index = 0
s[sy][sx] = "*"

for t_now in range(100):
    if time_index < n and str(t_now) == time_lr[time_index][0]:
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

    if sx < 0 or sx >= int(w) or sy < 0 or sy >= int(h) or s[sy][sx] != ".":
        break
    else:
        s[sy][sx] = "*"
for row in s:
    print("".join(row))

# for y in range(int(h)):
#     for x in range(int(w)):
#         print(s[y][x], end="")
#     print()