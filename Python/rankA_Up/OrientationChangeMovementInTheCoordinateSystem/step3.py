# 開始時点の y , x 座標 と向いている方角 D が与えられます。
# 続く 1 行で移動の向き d が与えられるので、その向きに移動した後の y , x 座標 を答えてください。
# 移動前に向いている方角によって同じ移動の向きでも座標の変化が違うことに気をつけてください。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。
# 以下の図を参考にしてみてください。


y,x,d = input().split()
y = int(y)
x = int(x)
lr = input()

if d == "N":
    if lr == "R":
        x += 1
    elif lr == "L":
        x -= 1
elif d == "S":
    if lr == "R":
        x -= 1
    elif lr == "L":
        x += 1
elif d == "E":
    if lr == "R":
        y += 1
    elif lr == "L":
        y -= 1
elif d == "W":
    if lr == "R":
        y -= 1
    elif lr == "L":
        y += 1
print(y,x)


# 解答2
y, x, now_direction = input().split()
y = int(y)
x = int(x)
d = input()
lr = 1

if d == "L":
    lr = -1

if now_direction == "N":
    x += lr
elif now_direction == "E":
    y += lr
elif now_direction == "S":
    x -= lr
elif now_direction == "W":
    y -= lr

print(y, x)