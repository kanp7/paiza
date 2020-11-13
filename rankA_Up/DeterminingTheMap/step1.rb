# 行数 H , 列数 W の盤面があり、各マスには文字が 1 つだけ書かれています。盤面と N 個の y , x 座標 が与えられるので、与えられた座標の文字を順に出力してください。

# なお、マスの座標系は左上端のマスの座標を ( y , x ) = ( 0 , 0 ) とし、
# 下方向が y 座標の正の向き、右方向が x 座標の正の向きとします。

h, w, n = gets.chomp.split(" ").map(&:to_i)
board = []

h.times do
    board << gets.chomp.split("")
end
# [["#", "#", "#"], ["#", "#", "#"], [".", ".", "."]]

coordinate = []
n.times do
    coordinate << gets.chomp.split(" ").map(&:to_i)
end
# [[2, 2], [1, 1]]

coordinate.each do |y, x|
    puts board[y][x]
end
