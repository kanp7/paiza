# あなたはとある試験の合格判定をする仕事をします。
# この試験は80点以上だと合格となります。

# 解答者の得点が与えれますので、合格か不合格を出力してしてください。

n = gets.to_i

if n >= 80
    puts "pass"
else
    puts "fail"
end