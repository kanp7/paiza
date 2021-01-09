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
    