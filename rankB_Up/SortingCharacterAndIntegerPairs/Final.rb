# 1行目に行数を表す整数 n、続く n 行の各行で「文字」と「整数」の組が空白区切りで入力されます。
# n 個の組を、「整数」の値で昇順に並べ変え、「文字」を出力してください。

n = gets.to_i
list = {}

n.times do
    s, d =  gets.chomp.split(" ")
    d = d.to_i
    list[s] = d
end
# {"A"=>1, "B"=>2}

sorted_list = list.invert.sort.to_h
# invertメソッドによりkeyとvalueを入れ替え、sortメソッドでkeyを昇順（小→大）、to_hメソッドで配列からハッシュに戻す。
# {1=>"A", 2=>"B"} 
puts sorted_list.values

# 回答例2
num = gets.chomp.to_i
array = {}

(1..num).each do
  line = gets.chomp.split(' ')
  array[line[1].to_i] = line[0]
end

array = array.sort

array.each do |ele|
  puts ele[1]
end