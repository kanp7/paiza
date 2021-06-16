# グリッド状の盤面の左上からスタートして、「右、下、右、上、左」と順に移動したときの経路上のマスのコストの合計を求めてください。

# 経路上のマスには、スタートとゴールのマスも含むものとします。

h, w = list(map(int,input().split()))

board = []
for _ in range(h):
    row = list(map(int,input().split()))
    board.append(row)

lr = 0
ud = 0
ans = 0
orders = ("右、下、右、上、左").split("、")
for order in orders:
    if order == '右':
        lr += 1
    elif order == '左':
        lr -= 1
    elif order == '上':
        ud += 1
    elif order == '左':
        ud -= 1
    ans += board[ud][lr]
print(ans)