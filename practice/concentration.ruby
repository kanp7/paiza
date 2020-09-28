data = gets.split(" ").map(&:to_i)
height = data[0]
width  = data[1]
player = data[2]
​
# ゲームの盤面を設定
game_field = []
height.times do
    game_field << gets.chomp.split(' ').map(&:to_i)
end
​
# 全部で何ターンあるかカウント
turn_count = gets.to_i
choice = []
​
# ターンの分、めくりかたの内容を配列化
turn_count.times do
    choice << gets.chomp.split(' ').map(&:to_i)
end
​
# プレイヤーの持ち点を初期化
player_point = []
player.times{player_point << 0}
​
# game_count:プレイヤーの順番
# 間違えた回数が人数になったら、最初の人に切り替える必要があるためmiss_countの設定
game_count, miss_count = 0,0
​
choice.each do |f|
    first_turn   = game_field[f[0] - 1][f[1] - 1]
    secound_turn = game_field[f[2] - 1][f[3] - 1]
​
    # 同じカードだったらポイントを増やし、次の番へ
    if first_turn == secound_turn
        player_point[game_count] += 2 
        next
    # プレイヤーの移動、間違えた回数のアップ
    else
        game_count += 1
        miss_count += 1
    end
    
    # もし、間違えた回数が人数になったら、ポイントもらう人を切り替える（最初に戻るから）
    if miss_count == player
        game_count, miss_count = 0,0
    end
end
​
puts player_point

# ------------------------

H, W, N = gets.split(' ').map(&:to_i)
​
field = []
H.times do
    field << gets.split(' ').map(&:to_i)
end
​
L = gets.to_i
# プレイヤー毎の取った枚数を記録する
player_score = (1..N).map { |x| [x, 0] }.to_h
# 今手番のプレイヤー
player = 1
L.times do
    # indexとして使えるように、全てから1を引いておく
    choice = gets.split(' ').map { |x| x.to_i - 1}
    card1 = field[choice[0]][choice[1]]
    card2 = field[choice[2]][choice[3]]
    if card1 == card2
        player_score[player] += 2
    else
		# ミスだった場合は手番が変わる
        if player == N
            player = 1
        else
            player += 1
        end
    end
end
​
puts player_score.values

# ------------------------