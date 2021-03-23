# N 人の人々がおり、それぞれの人は金と銀を何キログラムか持っています。今は金の方が銀よりも価値が高いですが、ある日金と銀の価値が逆転して、人々の財産の多さは次のように決定されるようになりました。

# 1. 持っている銀が多い方が財産が多い。
# 2. 持っている銀が同じなら、持っている金が多い方が財産が多い。

# それぞれの人が持っている金と銀のキログラム数が与えられるので、この規則にしたがって、財産を多い順に並び替えて出力してください。

# 入力される値
# 入力は以下のフォーマットで与えられます。

# N
# g_1 s_1
# ...
# g_N s_N

# 1 行目には人々の数を表す整数 N が与えられ、 2 行目から (N + 1) 行目には、人々が持っている金の量 g_i と銀の量 s_i がそれぞれ半角スペース区切りで N 行与えられます （1 ≤ i ≤ N）。

# 期待する出力
# 上の規則に従って人々の財産を並び替え、入力と同じ形式で、各 g_i, s_i を半角スペース区切りで、財産が多い順に N 行出力してください。
# 末尾に改行を入れ、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 ≤ N ≤ 50
# ・0 ≤ g_i, s_i ≤ 50（1 ≤ i ≤ N）

n = gets.to_i
array = n.times.map{gets.split(" ").map(&:to_i)}
# p array [[2, 1], [1, 2]]
sorting = array.sort{|a,b| (b[1]<=>a[1]).nonzero? || (b[0]<=>a[0])}

sorting.each do |x|
    puts x.join(" ")
end

# 回答2
count = gets.to_i
array = []
count.times do
    array << gets.split(' ').map(&:to_i)
end
array.sort! { |a, b|  (b[1] <=> a[1]).zero? ? b[0] <=> a[0] : b[1] <=> a[1]}
array.each do |a|
    puts a[0].to_s + " " + a[1].to_s
end