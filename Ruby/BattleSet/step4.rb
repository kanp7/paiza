# 明日からn日分の天気を占うために「明日天気にな〜れ」をすることにしました。

# 足に履いている靴の片方を蹴り上げて、靴が表向きだったら「晴れ」、裏向きだったら「雨」、横向きだったら「曇り」であるとします。

# 靴を蹴り上げた後の向きがn個入力されるので、n日分の天気占いの結果を出力してください。

n = gets.to_i

direction = []
n.times do 
    direction << gets.chomp
end

direction.each do |d|
    case d
    when "forward"
        puts "Sunny"
    when "reverse"
        puts "Rainy"
    when "sideways"
        puts "Cloudy"
    end
end
