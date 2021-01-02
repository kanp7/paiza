# 長さNの文字列Sが与えられます。Sに含まれている各文字の出現回数をそれぞれ求め、「a」の出現回数、「b」の出現回数、...、「z」の出現回数を順に半角スペース区切りで出力してください。

n = gets.to_i
s = gets.chomp.split("")

alp = ("a".."z").to_a
ans = []

alp.each do |i|
    count = 0
    s.each do |j|
        if i == j
            count +=1
        end
    end
    ans << count
end

puts ans.join(" ")