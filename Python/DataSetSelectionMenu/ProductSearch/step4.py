# paiza 商店には N 個の商品が売られており、i 番目の商品の名前は A_i で価格は B_i です。あなたはほしい M 個の商品名のリスト S を持っています。それぞれ paiza 商店ではいくらで売られているか答えてください。売られていない場合は -1 を出力してください。

n, m = map(int,input().split())
dic = {}
for _ in range(n):
    product, price = input().split()
    dic[product] = price
# {'eraser': '50', 'pencil': '30', 'book': '100'}

wants = []
for _ in range(m):
    wants.append(input())
# ['book', 'eraser', 'pencil', 'margaret']

for i in wants:
    if i in dic:
        print(dic[i])
    else:
        print("-1")
    
