# 配列 A の要素数 N と整数 K , 配列 A の各要素 A_1 ... A_N が与えられるので、K 以上であるような配列 A の要素のみを要素として持つ配列 B を作成し、その要素を出力してください。 B の要素の順は A と同じにしてください。

n, k = gets.chomp.split(" ").map(&:to_i)

n.times do
    i = gets.to_i
    if i >= k
        puts i
    end
end    