# 5行5列の五目並べの盤面が与えられます。

# 盤面の各マスには、"O"か"X"か"."が書かれています。

# "O"と"X"は、それぞれプレイヤーの記号を表します。

# 同じ記号が縦か横か斜めに連続で5つ並んでいれば、その記号のプレイヤーが勝者となります。

# 勝者の記号を1行で表示してください。
# 勝者がいない場合は、引き分けとして、"D"を表示してください。

board = []
player = [ "O", "X"]
result = "D"

5.times do 
    board << gets.chomp.split("")
end


# 横の判定
player.each do |p|
    board.each do |row|
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

# 縦の判定
vertical = []
5.times do |r|
    column = []
    5.times do |c|
        column << board[c][r]
    end
    vertical << column
end

player.each do |p|
    vertical.each do |column|
        count = 0
        column.each do |i|
            if i == p
                count += 1
            end
        end
        
        if count == 5
            result = p
        end
    end
end

# 斜めの判定
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

# 回答例2

$board = []

# 盤面の初期化
(1..5).each { $board.push(gets.chomp.split('')) }

def aligned?(o, x)
  if o == 5
    'O'
  elsif x == 5
    'X'
  else
    'D'
  end
end

def row_aligned?
  result = ''

  $board.each do |row|
    o = 0
    x = 0
    (0..4).each do |i|
      if row[i] == 'O'
        o = o + 1
      elsif row[i] == 'X'
        x = x + 1
      else
        break
      end
    end

    result = aligned?(o, x)
    break if result != 'D'
  end

  result
end

def collum_aligned?
  result = ''

  (0..4).each do |i|
    o = 0
    x = 0
    $board.each do |row|
      if row[i] == 'O'
        o = o + 1
      elsif row[i] == 'X'
        x = x + 1
      end
    end

    result = aligned?(o, x)
    break if result != 'D'
  end

  result
end

def oblique_aligned?
  result = ''

  (0..1).each do |time|
    i = 0

    if time.zero?
      j = 0
    else
      j = 4
    end

    o = 0
    x = 0
    (1..5).each do
      if $board[i][j] == 'O'
        o = o + 1
      elsif $board[i][j] == 'X'
        x = x + 1
      end

      i = i + 1

      if time.zero?
        j = j + 1
      else
        j = j - 1
      end
    end

    result = aligned?(o, x)
    break if result != 'D'
  end

  result
end

if row_aligned? == 'O' || collum_aligned? == 'O' || oblique_aligned? == 'O'
  puts 'O'
elsif row_aligned? == 'X' || collum_aligned? == 'X' || oblique_aligned? == 'X'
  puts 'X'
else
  puts 'D'
end