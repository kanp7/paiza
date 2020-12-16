# 昨日と比べて、今日の気温が高いのか低いのかを教えてくれるプログラムを作成したいと思いました。

# 昨日の気温と今日の気温が入力として与えられるので、

# 気温がどれだけ変化したかを計算して出力してください。

t1, t2 = gets.split.map(&:to_i)

ans = t2 - t1

if ans > 0
    puts "+"+ans.to_s
elsif ans == 0
    puts "0"
else
    puts ans.to_s
end