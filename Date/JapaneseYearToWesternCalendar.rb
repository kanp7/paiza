# 西暦年y、月m、日付dが与えられるので、和暦の元号を表示してください。

# 和暦は、以下の条件を確認し、西暦から変換してください。
# ・明治は1912年7月29日まで
# ・大正は1912年7月30日から1926年12月24日まで
# ・昭和は1926年12月25日から1989年1月7日まで
# ・平成は1989年1月8日から2019年4月30日まで
# ・令和は2019年5月1日から


y, m, d = gets.chomp.split(" ").map(&:to_i)

if y < 1912 || ( y == 1912 && m <= 7 && d <= 29) 
    y = "明治年"
elsif (y >= 1912 && m >8 || y >= 1912 && m ==7 && d >= 30)  && ( y<= 1926 )
    y = "大正年"
elsif y >= 1926 && (y <= 1989 && m == 1 && d <= 7)
    y = "昭和年"
elsif y >= 1989 && (y <= 2019 && m <= 4 && d <= 30)
    y = "平成年"
else y >= 2019 && m >= 5 
    y = "令和年"
end

puts "#{y}#{m}月#{d}日"

# 回答例2
y, m, d = gets.split.map(&:to_i)

date_number = y * 10_000 + m * 100 + d

era =
  case date_number
  when 1873_01_01..1912_07_29
    '明治'
  when 1912_07_30..1926_12_24
    '大正'
  when 1926_12_25..1989_01_07
    '昭和'
  when 1989_01_08..2019_04_30
    '平成'
  when 2019_05_01..3000_12_31
    '令和'
  end

puts "#{era}年#{m}月#{d}日"