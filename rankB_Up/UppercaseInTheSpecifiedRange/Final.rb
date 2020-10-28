# スペース区切りの2つの整数と、文字列が入力されます。2つの整数の範囲の部分文字列を、大文字にして出力してください。

n = gets.split(" ")
a = n[0].to_i - 1
b = n[1].to_i - 1

s = gets.chomp

ans = []
s.size.times do |i|
    if i >= a && i <= b
      ans << s[i].upcase
    else
      ans << s[i]
    end
end

puts ans.join()
