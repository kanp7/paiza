# 1行目で血液型が1つ与えられます。
# m 行の血液型と占い結果の組が与えられるので、血液型をキー、占い結果を値として、連想配列（辞書）に保存してください。
# その後、1行目で与えられた血液型に対応する占い結果を表示してください。

blood = gets.chomp

# hash = { A: :Good, B: :veryGood, O: :Yavai, AB: :VeryYabai }
hash = {}

# m行の部分でエラーが発生してしまう
4.times do
    key, value = gets.chomp.split(" ")
    hash[key] = value
end
puts hash[blood]

# 回答
blood_type = gets.chomp
fortunes = {}

while tmp = gets do
    tmp = tmp.chomp.split(" ")
    fortunes[tmp[0]] = tmp[1]
end

puts fortunes[blood_type]

# 回答2
blood = gets.chomp

4.times do
    key, value = gets.chomp.split(" ")
    if key == blood
        puts value
        break
    end
end