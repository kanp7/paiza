# K さんは paiza のアカウントを作成することにしました。そのためには、パスワードの設定が必要なことがわかりました。
# そこで K さんは忘れないように、次のようなルールにのっとって N 文字のパスワードを設定することにしました。

# ・ ルール
# K さんは N 文字のうち、 Q 文字だけ覚えておく文字を決めておく。
# 具体的には n_i 文字目を c_i とだけ決めて、残りの全ての文字を C にする。

# K さんの設定したパスワードを当ててください。

# 例
# ・ N = 5 , Q = 1 , n_1 = 2 , c_1 = 'T' , C = 'K' のとき
# パスワードは 5 文字であり、 2 文字目が 'T' , それ以外の文字を 'K' としたものである "KTKKK" が K さんのパスワードとなる。

n = gets.to_i
q = gets.to_i

hash = {}
q.times do
    index ,word = gets.chomp.split(" ")
    index = index.to_i
    hash[index]= word
end

m = gets.chomp

ans = ""
n.times do
    ans << m
end

hash.each do |index, word|
    ans[index-1] = word
end

puts ans