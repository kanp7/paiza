# 普通の鳩時計は 1 時間に 1 回しか鳴かないのでつまらないと思ったあなたは、鳩時計を改造してスーパー鳩時計を作りました。
# このスーパー鳩時計は時刻が x 時 y 分のとき x + y が 3の倍数のとき"FIZZ"、5 の倍数のとき"BUZZ", 3の倍数かつ5の倍数のとき "FIZZBUZZ" と鳴き、これらのいずれにも当てはまらなかった場合は鳴きません。
# なお、0 は 3 の倍数かつ 5 の倍数であるとします。 0 時 0 分　〜 23 時 59 分 の各分のスーパー鳩時計の様子を出力してください。

hour = (0..23)
minutes = (0..59)

hour.each do |x|
    minutes.each do |y|
        if (x + y) % 15 == 0
            puts "FIZZBUZZ"
        elsif (x + y) % 3 == 0
            puts "FIZZ"
        elsif ( x + y) % 5 == 0
            puts "BUZZ"
        elsif (x + y) == 0
            puts "FIZZBUZZ"
        else
          # 何故か空行が必要
            puts ""
        end
    end
end
