# 行数 H , 列数 W の盤面があり、盤面の各マスには文字が 1 つだけ書かれています。
# 盤面が与えられるので、「左右のマスが "#" 」であるようなマスの座標を全て出力してください。
# ただし、左端のマスの場合は「右のマスが "#" 」であれば、右端のマスの場合は「左のマスが "#" 」であれば条件を満たすものとします。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

hight, $wide = gets.chomp.split(" ").map(&:to_i)
$board = []

hight.times do
    $board << gets.chomp.split("")
end
# [["#", ".", "#"], [".", "#", "."], [".", ".", "."]]
def checking(h, w)
    check_place = []
    # 左端の場合
    if w == 0
        check_place << $board[h][1]
    # 右端の場合
    elsif w == ($wide -1)
        check_place << $board[h][w-1]
    # その他
    else
        check_place.push( $board[h][w-1],  $board[h][w+1] )
    end
    # true、falseを返す
    return check_place.all?{|mark| mark == "#"}
end

$board.each_with_index do |row, h|
    row.each_with_index do |mark, w|
        if checking(h,w)
            puts h.to_s + " " + w.to_s
        end
    end
end

# 回答例python
# coding: utf-8
​
H, W = map(int, input().split(' '))
​
field = []
for _ in range(H):
    field.append(input())
    
def check_holizontally(x, y):
    # 左端の場合
    if x == 0:
        checking_places = field[y][1]
    # 右端の場合
    elif x == W - 1:
        checking_places = field[y][x-1]
    # その他
    else:
        checking_places = field[y][x-1] + field[y][x+1]
​
    return all(map(lambda char: char == "#", checking_places))
​
for y in range(H):
    for x in range(W):
        if check_holizontally(x, y):
            print(y, x)