# N 個の文字列が入った、配列Sが与えられます。各 1 ≦ i ≦ Q に対して、以下の質問に答えてください。
# * 文字列T_iが与えられます。S_j == T_i となる最も小さな j を出力してください。ただし、Sの中にT_iがない場合は -1 を出力してください。

n,q = gets.split(" ").map(&:to_i)

s = []
n.times do 
    s << gets.chomp
end

t = []
q.times do
    t  << gets.chomp
end

t.each do |i|
    if s.include?(i)
        puts s.index(i) + 1
    else
        puts -1
    end
end