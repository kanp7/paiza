# n 行のユーザーと血液型の組が与えられるので、ユーザーをキー、血液型を値として、連想配列（辞書）に保存してください。
# そのあとで連想配列（辞書）をそのまま表示してください。

n = gets.to_i
name_blood = {}

n.times do
    name, blood =  gets.chomp.split(" ")
    name_blood[name] = blood
end

name_blood.each do |key, value|
    puts "#{key} #{value}"
end