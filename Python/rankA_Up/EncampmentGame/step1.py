# 盤面の情報が与えられます。現在プレイヤーのいるマスは '*' になっており、そのマスはプレイヤーの陣地です。

# プレイヤーは現在の陣地から上下左右に 1 マス移動することで到達できるマスをプレイヤーの陣地にします。

# プレイヤーの陣地を '*' にした盤面を出力してください。


# ランタイムエラー
h,w = list(map(int,input().split()))

x = 0
y = 0

board = []
for i in range(h):
    row = list(input())
    board.append(row)
    if "*" in row:
        y = i
        x = row.index("*")

if y >0 :
    board[y-1][x] = "*"
if y < h:
    board[y+1][x] = "*"
if x > 0:
    board[y][x-1] = "*"
if x <w:
    board[y][x+1] = "*"

for row in board:
    print("".join(row))

# 解答
H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]

flag_out = False
for y in range(H):
    for x in range(W):
        if s[y][x] == "*":
            if y > 0:
                s[y - 1][x] = "*"
            if y < H - 1:
                s[y + 1][x] = "*"
            if x > 0:
                s[y][x - 1] = "*"
            if x < W - 1:
                s[y][x + 1] = "*"
            flag_out = True
            break
    if flag_out:
        break

for y in range(H):
    print("".join(s[y]))
