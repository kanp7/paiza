# 5行5列の五目並べの盤面が与えられます。

# 盤面の各マスには、"O"か"X"か"."が書かれています。

# "O"と"X"は、それぞれプレイヤーの記号を表します。

# 同じ記号が斜めに連続で5つ並んでいれば、その記号のプレイヤーが勝者となります。

# 勝者の記号を1行で表示してください。
# 勝者がいない場合は、引き分けとして、"D"を表示してください。

board = []
player = [ "O", "X"]
result = "D"

5.times do 
    board << gets.chomp.split("")
end

left_diagonal = []
5.times do |i|
    left_diagonal << board[i][i]
end

right_diagonal = []
5.times do |i|
    right_diagonal << board[i][4-i]
end

check_mark = []
check_mark.push(left_diagonal,right_diagonal)

player.each do |p|
    check_mark.each do |row|
        count = 0
        row.each do |i|
            if i == p
                count += 1
            end
        end
        
        if count == 5
            result = p
        end
    end
end

puts result