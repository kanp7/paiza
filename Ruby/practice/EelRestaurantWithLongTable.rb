# # 未完成

# data = gets.split(" ").map(&:to_i)

# people_count = data[0]
# pair_count = data[1]

# chair = Array.new(people_count, "0")
# first_index = 0
# last_index = (chair.length) -1
# # 5

# # p chair
# # [false, false, false, false, false, false]

# tmp_array = []

# pair_count.times do |pair|
#     tmp_array << gets.split(" ").map(&:to_i)
# end
# # p tmp_array
# # [[3, 2], [1, 6], [2, 5]]

# tmp_array.each do |member_count, start_index|
#     # はみでる場合
#     if start_index-2+member_count > last_index
#         # 六人の席で四番目の椅子から四人座らせる
#         if chair[start_index-1..last_index].all?{|i| i == "0"} && chair[first_index..(member_count - (last_index - start_index-2))].all?{|i| i == "0"}
            
#             (start_index-1..last_index).times do |k|
#                 chair[start_index-1+k] = "1"
#             end
#             (first_index..(member_count - (last_index - start_index-2))).times do |k|
#                 chair[first_index + k] = "1"
#             end
#         end
#     end
        
#     # start_index -1 から membre_countまでがfalseだったら
#     if chair[start_index-1..start_index-2+member_count].all?{|i| i == "0"}
#         member_count.times do |j|
#             chair[start_index-1 + j] = "1"
#         end
#     end
# end
# puts chair.count("1")


data = gets.split(" ").map(&:to_i)

people_count = data[0]
pair_count = data[1]

seats = Array.new(people_count, "0")
# ["0", "0", "0", "0", "0", "0"]
first_index = 0
last_index = (seats.length) -1
# 5

tmp_array = []

pair_count.times do |pair|
    tmp_array << gets.split(" ").map(&:to_i)
end
# [[3, 2], [1, 6], [2, 5]]

tmp_array.each do |p_num, s_num|
    if seats[s_num-1..s_num-1+p_num-1].all?{|v| v == "0"}
        p_num.times do |i|
            seats[s_num-1+i] = "1"
        end
    end
end

p seats.count("1")