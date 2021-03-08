# 日時が "yyyy/MM/dd/hh:mm" の形式で与えられるので、年・月・日・時・分をそれぞれ出力してください。

n = gets.chomp.split("/")
m = n.last.split(":")
n.delete_at(-1)

puts  n,m