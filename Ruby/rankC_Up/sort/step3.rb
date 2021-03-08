# 正整数 n が与えられ、数のペアが n 個与えられます。各ペアの最初の数はりんごの個数を、その次の数はバナナの個数を表しています。これらの数のペアを以下の規則に従って、偉い順に並び替えてください。

# 1. ふたつのペアのりんごの数が異なる場合、りんごの数が多い方が偉い（この際、バナナの数は関係ない）。
# 2. りんごの数が同じである場合、バナナの数が多い方が偉い。

# 入力される値
# 入力は以下のフォーマットで与えられます。

# n
# a_1 b_1
# ...
# a_n b_n

# 1 行目に正整数 n が、 2 行目から (n + 1) 行目には半角スペース区切りの数のペア a_1 b_1, ..., a_n b_n が、それぞれ改行区切りで与えられます。

# 期待する出力
# ペアを偉い順に並べ替え、改行区切りで n 行、順に出力してください。出力の各行は入力と同じく、 "a_i b_i" のように、りんごの個数とバナナの数が、この順に、半角スペースで区切られているものとします。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・ 1 ≤ n , a_i, b_i ≤ 50 （1 ≤ i ≤ n）

n = gets.to_i

array = n.times.map{gets.split(" ").map(&:to_i)}
sorting = array.sort{|a,b| (b[0]<=>a[0]).nonzero? || (b[1] <=> a[1])}
# p sorting 	 [[2, 2], [1, 3]]
sorting.each do |x|
    puts x.join(" ")
end



# 回答2
def two_digit(num)
  num.length == 1 ? "0" + num : num
end

n = gets.to_i
  array = n.times.map{gets.split(" ").map{|x|two_digit(x)}}

p array

join_array  = array.map(&:join)

sorting_num = join_array.sort.reverse

p sorting_num

p sorting_num.map{|x|x.slice(2,2)}