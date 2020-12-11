# 西暦y年m月d日の次の日を表示してください。

# ただし、各月の日数は以下のように決まることに注意してください。
# ・4, 6, 9, 11月は30日
# ・2月は閏年ならば29日、そうでなければ28日
# ・それ以外の月は31日

# ただし、閏年は次のような年のことをいいます。
# ・西暦が4で割り切れる年は閏年
# ・ただし、100で割り切れる年は平年
# ・ただし、400で割り切れる年は閏年

y, m, c = gets.split(" ").map(&:to_i)

if (m == 4 || m == 6 ||  m == 9 || m == 11) && c == 30
    puts "#{y} #{m+1} #{1}"
elsif
    m == 2 && (y % 400 == 0 || y % 100 != 0 && y % 4 == 0) && c == 29
    puts "#{y} #{m+1} #{1}"
elsif
    m == 2 && c == 28
    puts "#{y} #{m+1} #{1}"
elsif c == 31
    if m == 12
        puts "#{y+1} #{1} #{1}"
    else
        puts "#{y} #{m+1} #{1}"
    end
else
    puts "#{y} #{m} #{c+1}"
end

# 回答例2
END_OF_MONTH = [
  [1, 31],
  [2, 29],
  [3, 31],
  [4, 30],
  [5, 31],
  [6, 30],
  [7, 31],
  [8, 31],
  [9, 30],
  [10, 31],
  [11, 30]
]

def is_leap?(y)
  (y % 400).zero? || (y % 100).nonzero? && (y % 4).zero?
end

def next_day(y, m, d)
  case [m, d]
  when [12, 31]
    [y + 1, 1, 1]
  when [2, 28]
    is_leap?(y) ? [y, 2, 29] : [y, 3, 1]
  when *END_OF_MONTH
    [y, m + 1, 1]
  else
    [y, m, d + 1]
  end
end

y, m, d = gets.split.map(&:to_i)

puts '%d %d %d' % next_day(y, m, d)