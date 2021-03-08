# 野球の各打者はストライクが 3 つたまるとアウトとなり、ボールが 4 つたまるとフォアボールとなります。
# アウトあるいはフォアボールになると、この打者の番は終了します。

# あなたはストライクとボールを判定してコールする審判です。
# その場の状況に合わせて適切なコールを出しましょう。

# 【コール一覧】
# ストライクが 1 〜 2 つたまったとき → "strike!"
# ストライクが 3 つたまったとき → "out!"
# ボールが 1 〜 3 つたまったとき → "ball!"
# ボールが 4 つたまったとき → "fourball!"

n = gets.to_i
call = []

n.times do |i|
    call << gets.chomp
    if call.count("strike") == 3
        puts "out!"
        call.clear
    elsif call.count("ball") == 4
        puts "fourball!"
        call.clear
    else
        puts call[i] + "!"
    end
end