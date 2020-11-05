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
