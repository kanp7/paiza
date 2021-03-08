# 正しい数式を表す文字列 S が与えられるので、その数式を計算した結果を出力してください。
# ただし、出てくる計算は足し算・引き算のみとし、数式に出てくる数字は全て 1 桁であるものとします。

# ・ 例
# ・ S = "1+1"
# 答えは 2 となります。

# ・ S = "4+3-2+1"
# 答えは 6 となります。

string = gets.chomp.split("")

num =[]
mark = []
string.each_with_index do |s,i|
    if i.even? == true
        num << s.to_i
    else
        mark << s
    end
end

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
