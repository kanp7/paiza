# 正しい数式を表す文字列 S が与えられるので、その数式を計算した結果を出力してください。ただし、出てくる計算は足し算・引き算のみとします。

# ・ 例
# ・ S = "1+1"
# 答えは 2 となります。

# ・ S = "4+3-2+1"
# 答えは 6 となります。

s = gets.chomp
num = s.chomp.split(/[+|-]/).map(&:to_i)
# [123, 456, 789]
mark = s.scan(/[+|-]/)
# ["+", "+"]

ans = 0
mark.length.times do |i|
    if i == 0
        if mark[i] == "+"
            ans = num[i] + num[i+1]
        else
            ans = num[i] - num[i+1]
        end
    end
    if i > 0
        if mark[i] == "+"
            ans += num[i+1]
        else
            ans -= num[i+1]
        end
    end
end

p ans