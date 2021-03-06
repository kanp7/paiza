
# 西暦y年m月d日が何曜日か表示してください。

# ただし、各月の日数は以下のように決まることに注意してください。
# ・4, 6, 9, 11月は30日
# ・2月は閏年ならば29日、そうでなければ28日
# ・それ以外の月は31日

# ただし、閏年は次のような年のことをいいます。
# ・西暦が4で割り切れる年は閏年
# ・ただし、100で割り切れる年は平年
# ・ただし、400で割り切れる年は閏年

# ただし、1800年1月1日は水曜日です。

y, m, d = gets.split.map(&:to_i)

require "date"

date = Date.new(y, m, d)
day_of_the_week = %w(日曜日 月曜日 火曜日 水曜日 木曜日 金曜日 土曜日)
# wdayメソッドは戻り値を数字で返す
puts day_of_the_week[date.wday]


# 回答例2
DAYS_OF_WEEK = %w[日曜日 月曜日 火曜日 水曜日 木曜日 金曜日 土曜日]

def is_leap?(y)
  (y % 400).zero? || (y % 100).nonzero? && (y % 4).zero?
end

# 30日 × m月 の計算をしているので31日ある月数分は調整して加算する
adjust_by_month = [0, 1, -1, 0, 0, 1, 1, 2, 3, 3, 4, 4]

y, m, d = gets.split.map(&:to_i)

# 閏年が何回来たか
leap_years = (y / 4 - y / 100 + y / 400)

# y年の時点で何日経過しているか
days = 365 * y + leap_years
# y年m月m日時点で何日経過しているか
days += (m - 1) * 30 + d - 1 + adjust_by_month[m - 1]
# 閏年の1月、2月の場合は1日分マイナスする
days -= 1 if is_leap?(y) && m < 3

puts DAYS_OF_WEEK[days % 7]