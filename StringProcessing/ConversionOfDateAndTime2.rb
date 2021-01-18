# 日時が "yyyy/MM/dd hh:mm" の形式で与えられるので、年・月・日・時・分をそれぞれ出力してください。


day, time = gets.chomp.split(" ")
y,m,d = day.split("/")
h,minu = time.split(":")

puts y,m,d,h,minu