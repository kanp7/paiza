# 1行目でユーザーが1つ与えられます。
# n 行のユーザーと血液型の組が与えられるので、ユーザーをキー、血液型を値として、連想配列（辞書）に保存してください。
# その連想配列（辞書）の中で1行目で与えられたユーザー名と、ユーザー名に対応する血液型を表示してください。

user = gets.chomp
n = gets.to_i
hash = {}

n.times do 
    key, value = gets.chomp.split(" ")
    hash[key] = value
end

puts "#{user} #{hash[user]}"