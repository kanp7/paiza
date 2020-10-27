# 10000 以上かつ 13 で割り切れるような最小の自然数を求めてください。

# 回答1
n = 10000
while n < 10013
    if n % 13 == 0
        puts n
    end
    n += 1
end

# 回答2
number = 10000
until number % 13 == 0 do
    number += 1
    if number % 13 == 0
      puts number
    end
end

# 回答3
number = 10000
loop{
    number += 1
    if number % 13 == 0
      puts number
    break
    end
    
}

# 回答4
array = []

for num in 10001..99999 do
  if num % 13 == 0
    array << num
  end
end

puts array.min