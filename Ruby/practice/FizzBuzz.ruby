# 整数 N が入力として与えられます。

# 1からNまでの整数を1から順に表示してください。

# ただし、表示しようとしている数値が、

# ・3の倍数かつ5の倍数のときには、"Fizz Buzz"
# ・3の倍数のときには、"Fizz"
# ・5の倍数のときには、"Buzz"

# を数値の代わりに表示してください

# 入力される値
# 入力は以下のフォーマットで与えられます。

# N

# N は1以上N以下の整数です。

# 期待する出力
# 最後は改行し、余計な文字、空行を含んではいけません。

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 ≦ N ≦ 100
# ・N は整数

N = gets.chomp.to_i
num = 0
for num in 0..(N-1) do
    num += 1
    if (num % 3 ==0 && num % 5 == 0)
        puts "Fizz Buzz"
    elsif (num % 3 == 0)
        puts "Fizz"
    elsif (num % 5 == 0)
        puts "Buzz"
    else
        puts num
    end
end

input = gets
input_number = input.to_i
(1..input_number).each do |n|
    if n % 15 == 0
        puts "Fizz Buzz"
    elsif n % 3 == 0
        puts "Fizz"
    elsif n % 5 == 0
        puts "Buzz"
    else
        puts n
    end
end
