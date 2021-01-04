# paiza 商店には N 個の商品が売られており、i 番目の商品の名前は A_i で価格は B_i です。あなたはほしい M 個の商品名のリスト S を持っています。それぞれ paiza 商店ではいくらで売られているか答えてください。売られていない場合は -1 を出力してください。


n,m = gets.split(" ").map(&:to_i)

items = []
n.times do
    item = gets.chomp.split(" ")
    items << item
end

items = items.to_h

wants = []
m.times do
    wants << gets.chomp
end

wants.each do |name|
    if items.include?(name)
        puts items[name]
    else
        puts -1
    end
end