# るスーパーでは、お一人様一点限りでセール価格の商品を販売することにしました。

# そこで、一人のお客さんが２回以上その商品を買えないように、お客さんの名前をチェックすることにしました。

# お客さんの名前が来た順番で入力されるので、そのお客さんが初めて来たのかどうかを判定し、結果を出力してください。

n = gets.to_i

names = []
n.times do 
    name = gets.chomp
    unless names.include?(name)
        names << name
        puts "YES"
    else
        puts "NO"
    end
end