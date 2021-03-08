# N 個の要素からなる数列Aが与えられます。 2 ≦ i ≦ Nの各iに対して、A_iと同じ値が、A_1 からA_( i - 1 )の間にあるか判定してください。

n = gets.to_i
array = gets.split.map(&:to_i)

numbers = []
array.each_with_index do |a,i|
    if i > 0
        if numbers.include?(a)
            puts "Yes"
        else
            puts "No"
        end
    end
    numbers << a
end
    