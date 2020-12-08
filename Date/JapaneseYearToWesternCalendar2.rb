# 西暦年y、月m、日付dが与えられるので、和暦で表示してください。

# 和暦は、以下の条件を確認し、西暦から変換してください。
# ・明治は1912年7月29日まで
# ・大正は1912年7月30日から1926年12月24日まで
# ・昭和は1926年12月25日から1989年1月7日まで
# ・平成は1989年1月8日から2019年4月30日まで
# ・令和は2019年5月1日から

y, m, d = gets.split(" ").map(&:to_i)

date_number = y * 10_000 + m * 100 + d

  case date_number
  when 1873_01_01..1912_07_29
    era = '明治' 
    y = y - 1868
        if y == 0
            y = "元"
        else
            y += 1
        end
  when 1912_07_30..1926_12_24
    era = '大正'
    y = y - 1912
        if y == 0
            y = "元"
        else
            y += 1
        end
  when 1926_12_25..1989_01_07
    era = '昭和'
    y = y - 1926
        if y == 0
            y = "元"
        else
            y += 1
        end
  when 1989_01_08..2019_04_30
    era = '平成'
        y = y - 1989
        if y == 0
            y = "元"
        else
            y += 1
        end
  when 2019_05_01..3000_12_31
    era = '令和'
        y = y - 2019
        if y == 0
            y = "元"
        else
            y += 1
        end
  end
puts "#{era}#{y}年#{m}月#{d}日"

# 回答例2

# メソッドの返り値を代入するため、yはグローバル変数にする
@y, m, d = gets.split(" ").map(&:to_i)

date_number = @y * 10_000 + m * 100 + d

# メソッド化
def check(input_year,first_year)
    @y = input_year - first_year
        if @y == 0
            @y = "元"
        else
            @y += 1
        end
end

  case date_number
  when 1873_01_01..1912_07_29
    era = '明治' 
    check(@y,1868)
  when 1912_07_30..1926_12_24
    era = '大正'
    check(@y,1912)
  when 1926_12_25..1989_01_07
    era = '昭和'
    check(@y,1926)
  when 1989_01_08..2019_04_30
    era = '平成'
    check(@y,1989)
  when 2019_05_01..3000_12_31
    era = '令和'
    check(@y,2019)
  end
puts "#{era}#{@y}年#{m}月#{d}日"