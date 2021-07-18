# あるスーパーでは、お一人様一点限りでセール価格の商品を販売することにしました。

# そこで、一人のお客さんが２回以上その商品を買えないように、お客さんの名前をチェックすることにしました。

# お客さんの名前が来た順番で入力されるので、そのお客さんが初めて来たのかどうかを判定し、結果を出力してください。

n = int(input())

names = []
for _ in range(n):
    name = input()
    if name in names:
        print("NO")
    else:
        names.append(name)
        print("YES")


# setの方が良いかも
n = int(input())

names = set()
for _ in range(n):
    name = input()
    print("NO") if name in names else print("YES")
    names.add(name)