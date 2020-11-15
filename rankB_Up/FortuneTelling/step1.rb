# 次のような「ユーザー」と「ユーザーに対応する血液型」を連想配列（辞書）として定義して、それらのキーと値のペアを順に出力してください。

hash = { Kyoko:	:B, Rio: :O, Tsubame: :AB, KurodaSensei: :A	, NekoSensei: :A }
hash.each do | name, blood|
    puts name.to_s + " " + blood.to_s
end

# 回答例2
user2blood = {'Kyoko' => 'B', 'Rio' => 'O', 'Tsubame' => 'AB', 'KurodaSensei' => 'A', 'NekoSensei' => 'A'}
user2blood.each do |user, blood|
  puts "#{user} #{blood}"
end