# 5行5列の五目並べの盤面が与えられます。

# 盤面の各マスには、"O"か"X"か"."が書かれています。

# "O"と"X"は、それぞれプレイヤーの記号を表します。

# 同じ記号が横に連続で5つ並んでいれば、その記号のプレイヤーが勝者となります。

# 勝者の記号を1行で表示してください。
# 勝者がいない場合は、引き分けとして、"D"を表示してください。

board = []
player = [ "O", "X"]
result = "D"

5.times do 
    board << gets.chomp.chars
end
    
board.each do |row|
    player.each do |p|
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
