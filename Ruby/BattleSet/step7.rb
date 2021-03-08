# あなたは奇数が大好きな山田さんと数字の仕分けをすることになりました。
# 仕分けをする数字が与えられますので、奇数であるものを小さい順に出力してください。

n = gets.to_i
numbers = []
n.times do 
    numbers << gets.to_i
end

odds = []
numbers.each do |i|
    if i.odd?
        odds << i
    end
end

puts odds.sort