# 縦Hマス、横Wマスの H × W マスからなる迷路があります。上からi行目、左からj列目のマス はS_ijとあらわされ、 S_ijが「#」のとき壁であり、「.」のとき道です。自然数r、cが与えられるので、S_rcが壁かどうか判定してください。

h,w,r,c = list(map(int,input().split()))
board = []
for _ in range(h):
    tmp = list(input())
    board.append(tmp)
# [['.', '.', '#', '.'], ['#', '.', '#', '#'], ['.', '.', '.', '.']]

ans = "Yes" if board[r-1][c-1] == "#" else "No"
print(ans)