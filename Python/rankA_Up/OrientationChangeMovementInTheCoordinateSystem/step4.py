# 開始時点の x , y 座標と移動の歩数 N が与えられます。
# 以下の図のように時計回りに渦を巻くように移動を N 歩行った後の x , y 座標 を答えてください。

# なお、マスの座標系は下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


# リスト directions と、カウント変数 now_direction で移動方向の管理をしています。
# 移動を move という関数にすることでコードをみやすくしています。
# first で、その移動マス数が1回目かどうかを管理しています。
# 現在の移動マス数を count で、現在の方角へ進む最大のマス数を max_count で表します。
# 1マス移動するたびに count += 1 して、count == max_count になったら
# その移動マス数での移動が 1 回目の場合 → 方向転換をして、その回数でもう一度移動させます。
# その移動マス数での移動が 2 回目の場合 → 方向転換をして、移動回数を 1 増やして、移動させます。
x, y, n = map(int, input().split())
directions = ["E", "S", "W", "N"]
now_direction = 0
count = 0
max_count = 1
first = True

def move(direction, x, y):
    if direction == "N":
        y -= 1
    elif direction == "E":
        x += 1
    elif direction == "S":
        y += 1
    elif direction == "W":
        x -= 1
    return (x, y)


for _ in range(n):
    (x, y) = move(directions[now_direction], x, y)
    count += 1
    if first and count == max_count:
        first = False
        count = 0
        now_direction = (1 + now_direction) % 4
    elif count == max_count:
        first = True
        count = 0
        max_count += 1
        now_direction = (1 + now_direction) % 4


print(x, y)