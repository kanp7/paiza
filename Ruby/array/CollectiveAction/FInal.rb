# あなたは集団行動のリーダーです。次のような指示を出すことで様々な列の操作ができます。

# ・swap A B
# 先頭から A 番目の人と、先頭から B 番目の人の位置を入れ替える。
# ・reverse
# 列の前後を入れ替える。
# ・resize C
# 先頭から C 人を列に残し、それ以外の人を全員列から離れさせる。ただし、列が既に C 人以下の場合、何も行わない。

# 初め、列には番号 1 〜 N の N 人がおり、先頭から番号の昇順に並んでいます。(1, 2 , 3, ..., N)
# あなたの出した指示の回数 Q とその指示の内容 S_i (1 ≦ i ≦ Q) が順に与えられるので、全ての操作を順に行った後の列を出力してください。


n, q = gets.chomp.split(" ").map(&:to_i)
array = []

def reverse(array)
    array.reverse!
end

def swap(array, n, m)
    array[n-1], array[m-1] = array[m-1], array[n-1]
end

n.times do |i|
    array << i + 1
end

q.times do
    order = gets.chomp
    if order == "reverse"
        reverse(array)
    else other_order = order.split(" ")
        if other_order[0] == "resize"
            number = other_order[1].to_i
            array = array.slice!(0,number)
        else
            n, m = other_order[1].to_i, other_order[2].to_i
            swap(array,n,m)
        end
    end
end

puts array