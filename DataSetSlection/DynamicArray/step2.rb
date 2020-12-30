# 要素数Nの数列Aと要素数Qの数列B与えられます。 1 ≦ i ≦ Q の各iについて、i行目には以下の数値を出力してください
# * AのB_i番目の値を出力してください。

n = gets.to_i
a = gets.split.map(&:to_i)

q = gets.to_i
b = gets.split.map(&:to_i)

b.each do |i|
    puts a[i-1]
end