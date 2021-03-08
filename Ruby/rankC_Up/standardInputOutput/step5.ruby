# 入力される値
# 入力は以下のフォーマットで与えられます。

# n

# 1行目に整数nが与えられます。

# 期待する出力
# paiza と n 回、半角スペース区切りで出力してください。最後の paiza の後には半角スペースは入れず、改行を入れ、余計な文字、空行を含んではいけません。

# paiza paiza ... paiza

# 条件
# すべてのテストケースにおいて、以下の条件をみたします。

# ・1 ≦ n ≦ 50

input = gets.to_i
n = input - 1
n.times do
  print "paiza "
end
print "paiza"