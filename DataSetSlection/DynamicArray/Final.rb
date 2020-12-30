# N 個の要素からなる数列Aが与えられます。A に対し、次の 3 つの操作をおこなうプログラムを作成してください。
# * push_back : Aの末尾にxを追加する
# * pop_back : Aの末尾を削除する
# * print : 数列Aを半角スペース区切りで出力する

n,q = gets.split().map(&:to_i)
a = gets.split().map(&:to_i)

q.times do 
    query = gets.split.map(&:to_i)
    if query.include?(0)
        a.push(query[1])
    elsif query.include?(1)
        a.pop
    elsif query.include?(2)
        puts a.join(" ")
    end
end

