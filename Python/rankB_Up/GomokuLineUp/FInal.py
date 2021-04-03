# 5行5列の五目並べの盤面が与えられます。

# 盤面の各マスには、"O"か"X"か"."が書かれています。

# "O"と"X"は、それぞれプレイヤーの記号を表します。

# 同じ記号が縦か横か斜めに連続で5つ並んでいれば、その記号のプレイヤーが勝者となります。

# 勝者の記号を1行で表示してください。
# 勝者がいない場合は、引き分けとして、"D"を表示してください。

board = []
for _ in range(5):
    row = list(input())
    board.append(row)
# board
# ['X', 'X', 'O', 'X', 'O']
# ['O', 'X', 'O', 'X', 'X']
# ['O', 'O', 'O', 'O', 'O']
# ['O', 'X', 'O', 'X', '.']
# ['X', 'O', 'X', 'X', 'O']

ver_to_hor = []
for i in range(5):
    tmp = []
    for j in range(5):
        tmp.append(board[j][i])
    ver_to_hor.append(tmp)
# ver_to_hor
# ['X', 'O', 'O', 'O', 'X'],
# ['X', 'X', 'O', 'X', 'O'],
# ['O', 'O', 'O', 'O', 'X'], 
# ['X', 'X', 'O', 'X', 'X'],
# ['O', 'X', 'O', '.', 'O']

diagonals = [[], []]
for i in range(5):
    # 右斜下方向
    diagonals[0].append(board[i][i])
    # 左斜下方向
    diagonals[1].append(board[i][4 - i])
# diagonals
# [['X', 'X', 'O', 'X', 'O'], ['O', 'X', 'O', 'X', 'X']]

def check_result(target):
    player = ['O','X']
    result = "D"
    for mark in player:
        for row in target:
            count = 0
            for i in row:
                if i == mark:
                    count += 1
            if count == 5:
                result = mark
    print(result)

check_result(board+ver_to_hor+diagonals)