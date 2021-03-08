# 検索ワード W が N 個与えられるので、N 個の検索ワードが与えられた後の履歴を表示するプログラムを書いてください。

# 検索ワード W が以前に入力されたことがある場合：
# 履歴中の W を削除する。
# 履歴の先頭に W を追加する。
# 検索ワード W が以前に入力されたことがない場合：
# 履歴の先頭に W を追加する。

n = gets.to_i

words = []

n.times do
    new_word = gets.chomp
    if words.include?(new_word)
        words.delete(new_word)
        # unshiftで配列の先頭に追加する
        words.unshift(new_word)
    else
        words.unshift(new_word)
    end
end

puts words
