# マップの行数 H と列数 W とマップを表す H 行 W 列の文字列 S_1 ... S_H が与えられるので、
# 隣接する上下左右のマスが全て '#' であるマスの y , x 座標 を答えてください。

# ただし、左端のマスの場合は「右のマスが '#' 」であれば、右端のマスの場合は「左のマスが '#' 」であれば隣接する左右のマスが全て '#' であるものとします。
# また、上端のマスの場合は「下のマスが '#' 」であれば、下端のマスの場合は「上のマスが '#' 」であれば隣接する上下のマスが全て "#" であるものとします。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h, w = map(int,input().split())

s = [list(input()) for _ in range(h)]
# print(s)  [['#', '#', '.'], ['#', '#', '#'], ['.', '.', '.']]

for y in range(h):
    for x in range(w):
        if y == 0 or s[y-1][x] == "#":
            if y == h-1 or s[y+1][x] == "#":
                if x == 0 or s[y][x-1] == "#":
                    if x == w-1 or s[y][x+1]== "#":
                        print(y, x)


# 解答2
h, w = map(int, input().split())
s = [list(input()) for _ in range(h)]

for y in range(h):
    for x in range(w):
        flag_row = False
        flag_column = False

        if x == 0 or s[y][x - 1] == "#":
            if x == w - 1 or s[y][x + 1] == "#":
                flag_row = True

        if y == 0 or s[y - 1][x] == "#":
            if y == h - 1 or s[y + 1][x] == "#":
                flag_column = True

        if flag_column and flag_row:
            print(y, x)