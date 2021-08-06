# マップの行数 H と列数 W とマップを表す H 行 W 列の文字列 S_1 ...S_H が与えられます。
# 要素が '#' になっているマスが 1 つあるので、その y , x 座標 を答えてください。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h, w = map(int,input().split())

board = []
for i in range(h):
    row = input()
    if "#" in row:
        print(i, row.index("#"))


# 解答2
H, W = map(int, input().split())
S = [list(input()) for _ in range(H)]

for y in range(H):
    for x in range(W):
        if S[y][x] == "#":
            print(y, x)