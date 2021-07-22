# 行数 H , 列数 W の盤面があり、各マスには文字が 1 つだけ書かれています。盤面と N 個 の y , x 座標 が与えられるので、盤面の与えられた座標の文字を "#" に書き換えた後の盤面を出力してください。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。


h,w,n = map(int,input().split())

coordinates = []
for _ in range(h):
    coordinates.append((list(input())))

for _ in range(n):
    y, x = map(int,input().split())
    coordinates[y][x] = "#"

for c in coordinates:
    print("".join(c))


# 解答例2
h, w, n = map(int, input().split())
s = [list(input()) for _ in range(h)]

for _ in range(n):
    y, x = map(int, input().split())
    s[y][x] = "#"

for y in range(h):
    print("".join(s[y]))