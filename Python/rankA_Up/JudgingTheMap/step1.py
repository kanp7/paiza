# 行数 H , 列数 W の盤面があり、各マスには文字が 1 つだけ書かれています。盤面と N 個の y , x 座標 が与えられるので、与えられた座標の文字を順に出力してください。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

h,w,n = list(map(int,input().split()))
coordinates = []
for _ in range(h):
    coordinates.append(input())
    
for _ in range(n):
    y, x = list(map(int,input().split()))
    print(coordinates[y][x])