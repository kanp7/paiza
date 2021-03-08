n = gets.chomp
# "123456789"

ans = n.reverse.scan(/.{1,#{3}}/).map(&:reverse)
# ["789", "456", "123"]

# 正規表現では「.」が改行を除く任意の1文字 として扱われる。
# {}の中で「それを何回繰り返すか」という数を指定。
# 今回のケースでは「1回以上最大3回」のため、 .{1,#{3}} 
# 参考URL
# https://tanarizm.com/ruby-string-scan

puts ans.reverse.join(",")