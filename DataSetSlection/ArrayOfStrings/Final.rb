# 縦Hマス、横Wマスの H × W マスからなる迷路があります。上からi行目、左からj列目のマス はS_ijとあらわされ、 S_ijが「#」のとき壁であり、「.」のとき道です。自然数r、cが与えられるので、S_rcが壁かどうか判定してください。

h,w,r,c = gets.split.map(&:to_i)

s = []
h.times do 
    s << gets.chomp.split("")
end

if s[r-1][c-1] == "#"
    puts "Yes"
else
    puts "No"
end
