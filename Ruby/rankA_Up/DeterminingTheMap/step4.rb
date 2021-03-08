# 行の数
count_lines  = gets.split.map(&:to_i)[0]
​
# 通常時：その行の上としたが#であるか？
# 例外時：最初と最後の行で上または下が#であるか？
# つまり、行の前後の行を見るから、多次元配列にすれば楽という考え
@field = []
​
# 多次元配列の完成 行が綺麗に分かれた
count_lines.times do
  @field << gets.chomp.split("")
end
​
# 最初の行の処理
def first_line(index)
  # 一個後の行を見にいく
  @field[index + 1].each_with_index do |f, index|
      puts "0" + " " + index.to_s if f == "#"
  end
end
​
# 最後の行の処理
def last_line(index)
  # 一個前を見にいく
  @field[index - 1].each_with_index do |f, index|
    puts (count_lines - 1).to_s + " " + index.to_s if f == "#"
  end
end
​
# 行ごとにチェックしていく
@field.each_with_index do |line, index|
  if index == 0
    first_line(index)
  elsif index == count_lines - 1
    last_line(index)
  else
    # 列の数だけ一個前と一個後の行を見る
    line.count.times do |tmp_index|
      if @field[index - 1][tmp_index] == "#" && @field[index + 1][tmp_index] == "#"
        puts index.to_s + " " + tmp_index.to_s
      end
    end
  end
end