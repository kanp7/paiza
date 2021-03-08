# 数値を表す文字列 S と 1 桁の数値 T が与えられるので、S * T の結果を表す文字列を出力してください。

s = gets.to_i
t = gets.to_i
puts s*t

# RUbyはオーバーフローしない

# 普通に S を数値として計算を行うとオーバーフローが発生します。
# そこで、S を文字列として受け取り、かけ算の処理を各桁ごとに分割します。
# 小さい位から順に、各桁の数字について S[i]*T を行って順に繰り上がりの処理を行います。
# 計算結果を数値として格納することもできないので、計算結果の各桁の数字を文字列として覚えておきます。
# 文字列から数値、数値から文字列の変換が重要な操作になります。
# どちらかに考えを引っ張られることなく、柔軟に変換ができることを意識してください。
# T == 0 の時は、答えが 0....0 の形式になってしまうので、例外的に処理してください。

s = gets.chomp

t = gets.to_i

len = s.length

adding = []
c = 0

if t == 0
    puts 0
else
    len.times do |i| 
        m = s.reverse[i].to_i * t
        if m >= 10
            m = m + c
            m = m.to_s
            m = m.split("")
            c = m[0].to_i
            if len == i + 1
                adding << m
            else
                adding << m[1]
            end
        else
            m = m + c
            if m >= 10
                m = m.to_s
                m = m.split("")
                c = m[0].to_i
                if len == i + 1
                    adding << m
                else
                    adding << m[1]
                end
            else
                m = m.to_s
                adding << m
                # 桁上りが発生しなかった場合、Cをリセットする
                c = 0
            end
        end
    end
    puts adding.reverse.join("")
end




