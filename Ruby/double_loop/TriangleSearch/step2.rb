# 配列 A の要素数 N とその要素 A_i (1 ≦ i ≦ N) が与えられるので、A についてのかけ算表 B を出力してください。かけ算表は N * N の二次元配列の形式とし、B の i 行 j 列の要素 B_ij について、B_ij = Ai * Aj (1 ≦ i , j ≦ N) が成り立つものとします。

# 例として、A = [1,2,3] のとき B は

# 1 2 3
# 2 4 6
# 3 6 9

# となります。

n = gets.to_i

array = gets.split(" ").map(&:to_i)

ans = []
n.times do |i|
    temp = []
    n.times do |j|
       temp <<  array[i] * array[j]
    end
    ans << temp.join(" ")
end

puts ans

