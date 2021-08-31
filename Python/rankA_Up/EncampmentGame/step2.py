# 盤面の情報が与えられます。現在プレイヤーのいるマスは '*' になっており、そのマスはプレイヤーの陣地です。

# プレイヤーは現在の陣地から上下左右に 1 マス移動することで到達できるマスをプレイヤーの陣地にします。
# ただし、障害物( '#' ) のあるマスは陣地にできません。

# プレイヤーの陣地を '*' にした盤面を出力してください。


H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

flag_out = False
for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            if y > 0 and s[y-1][x] != "#":
                s[y-1][x] = "*"
            if y < H - 1 and s[y+1][x] != "#":
                s[y+1][x] = "*"
            if x > 0 and s[y][x-1] != "#":
                s[y][x-1] = "*"
            if x < W - 1 and s[y][x+1] != "#":
                s[y][x+1] = "*"
            flag_out = True
            break
    if flag_out:
        break

for y in range(H):
    print("".join(s[y]))