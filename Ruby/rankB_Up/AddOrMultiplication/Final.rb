# スペース区切りの2つの整数がn行与えられるので、2つの整数をそれぞれ足し合わせて、さらに、その結果をすべての行について足し合わせて出力してください。
# ただし、2つの整数が同じだった場合は、2つの整数を掛け合わせてから、その結果を足し合わせてください。

n = gets.to_i

ans = 0
n.times do
    a, b = gets.split(" ").map(&:to_i)
    if a == b
        ans += a * b
    else
        ans += a + b
    end
end
puts ans

# 回答例2
n = gets.to_i

arrays = n.times.map{gets.split(" ", 2).map(&:to_i)}

answers = []

arrays.each{|array|
  if array[0] == array[1]
    answers << array[0] * array[1]
  else
    answers << array[0] + array[1]
  end
}

p answers.inject(:+)