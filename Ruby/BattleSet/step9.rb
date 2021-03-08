# ある図形に対し、線対称、点対称は次のように定義されます。
# ・線対称：ある直線を折り目にして折りたたんだとき、折り目の両側がぴったり重なること
# ・点対称：ある一点で180度回転させたとき、もとの図形とまったく同じ形になること

# この問題では、ドット絵に対する線対称、点対称を以下のように定義します。
# ・線対称：ドット絵の中心を通る垂直、または水平な直線で折りたたんだとき、折り目の両端がぴったり重なること
# （斜めの直線を折り目にすることは考えません。）
# ・点対称：ドット絵の中心で180度回転させたとき、もとの図形とまったく同じ形になること

# n×mのドット絵が入力されるので、そのドット絵が線対称であるか、点対称であるか、その両方か、そのどちらかでもないかを判定するプログラムを作成してください。
# h,w = gets.split.map(&:to_i)


# テストケース6以降が通らない
h,w = gets.split.map(&:to_i)

wide = []
h.times do 
    wide << gets.chomp.split("")
end

def check_line_symmetry_vertical(wide)
    count = 0
    loopcount = 0
    wide.each.with_index(1) do |row, index|
        loopcount = index
        if row.reverse == row
            count += 1
        end
    end

    if loopcount == count
        return true
    else
        return false
    end
end

def check_line_symmetry_horizontal(wide)
    flag = 0
    index = 0
    count = wide.count
    
    (wide.count/2).times do
        if wide[index] == wide[count-1]
            flag += 1
        end
        count -= 1
        index += 1
    end
    
    if flag == index
        return true
    else
        return false
    end
end

def check_point_symmetry(wide)
    point = []
    wide.reverse.each do |row|
        point << row.reverse
    end
    if wide == point
        return true
    else
        return false
    end
end

if (check_line_symmetry_vertical(wide) == true || check_line_symmetry_horizontal(wide)) && check_point_symmetry(wide) == true
    puts "line point symmetry"
elsif check_line_symmetry_vertical(wide) == true
    puts "line symmetry"
elsif check_line_symmetry_horizontal(wide) == true
    puts "line symmetry"
elsif check_point_symmetry(wide) == true
    puts "point symmetry"
else
    puts "none"
end