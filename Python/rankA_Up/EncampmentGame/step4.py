# 盤面の情報が与えられます。
# 現在プレイヤーのいるマスは '*' になっており、そのマスはプレイヤーの陣地です。

# プレイヤーは次の操作をできなくなるまで続けます。

# ・ プレイヤーは現在の陣地から上下左右に 1 マス移動することで到達できるマスをプレイヤーの陣地にする。ただし、障害物( '#' )のマスは陣地にできない。

# 操作を終えた後のプレイヤーの陣地のマスを、陣地にするまでの操作回数にしたマップを出力してください。
# なお、はじめにプレイヤーのいるマスの操作回数は 0 とします。


# 盤面の情報が与えられます。
# 現在プレイヤーのいるマスは '*' になっており、そのマスはプレイヤーの陣地です。

# プレイヤーは次の操作をできなくなるまで続けます。

# ・ プレイヤーは現在の陣地から上下左右に 1 マス移動することで到達できるマスをプレイヤーの陣地にする。ただし、障害物( '#' )のマスは陣地にできない。

# 操作を終えた後のプレイヤーの陣地のマスを、陣地にするまでの操作回数にしたマップを出力してください。
# なお、はじめにプレイヤーのいるマスの操作回数は 0 とします。


H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
my_p = []

flag_out = False
for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            s[y][x] = str(0)
            my_p.append([y, x, 1])

while len(my_p) > 0:
    [y, x, n] = my_p[0]
    my_p.pop(0)

    if y > 0 and s[y - 1][x] == ".":
        s[y - 1][x] = str(n)
        my_p.append([y - 1, x, n + 1])
    if y < H - 1 and s[y + 1][x] == ".":
        s[y + 1][x] = str(n)
        my_p.append([y + 1, x, n + 1])
    if x > 0 and s[y][x - 1] == ".":
        s[y][x - 1] = str(n)
        my_p.append([y, x - 1, n + 1])
    if x < W - 1 and s[y][x + 1] == ".":
        s[y][x + 1] = str(n)
        my_p.append([y, x + 1, n + 1])

for y in range(int(H)):
    print("".join(s[y]))
