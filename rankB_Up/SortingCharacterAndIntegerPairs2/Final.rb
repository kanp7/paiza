# 1行目に行数を表す整数 n、続く n 行の各行で「文字」と「整数」の組が空白区切りで入力されます。
# n 個の組について、「文字」の値が同じ組同士の数値を足しわせてまとめ、まとめた数値の降順で、文字とまとめた数値の組を出力してください。

n = gets.to_i
list = {}

n.times do
  s, d = gets.chomp.split(" ")
  d = d.to_i
  if list.keys.include?(s)
      d = list[s] + d
      list[s] = d
  else
      list[s] = d
  end
end
sorted_list = list.invert.sort.reverse.to_h
# {75=>"B", 11=>"A", 6=>"D", 4=>"G", 2=>"C"}

sorted_list.each do |integer, string|
    puts string + " " + integer.to_s
end

# 回答例2
n = gets.to_i

array = []
n.times do
    s, d = gets.chomp.split(" ")
    array <<  [s, d.to_i]
end
# [["A", 1], ["D", 6], ["C", 2], ["G", 4], ["B", 70], ["A", 10], ["B", 5]]

hash =  array.group_by(&:first).map{|k, v| [k, v.sum(&:last)]}.to_h
# {"A"=>11, "D"=>6, "C"=>2, "G"=>4, "B"=>75}

# list.group_by(&:first)部分の実行結果
# {"A"=>[["A", 1], ["A", 10]], "D"=>[["D", 6]], "C"=>[["C", 2]], "G"=>[["G", 4]], "B"=>[["B", 70], ["B", 5]]}
#.map部分の説明 | k=A,v=[["A", 1], ["A", 10]] | v（配列）の最後の要素、つまり数字を合計した値をvに代入している

sort = hash.sort_by { |k, v| v }.reverse.to_h
# {"B"=>75, "A"=>11, "D"=>6, "G"=>4, "C"=>2}

sort.each do |key, value|
  puts "#{key} #{value}"
end