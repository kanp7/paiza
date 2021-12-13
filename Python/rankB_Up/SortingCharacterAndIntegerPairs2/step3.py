# 指定された配列（リスト）の定義の中で、同じ要素の数をカウントして、その数を出力してください。

array = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]

count = 0

print(array.count("NGO"))

# 解答2
array = ["HND", "NRT", "KIX", "NGO", "NGO", "NGO", "NGO", "NGO"]
count = {}

for pattern in array:
    if pattern in count:
        count[pattern] += 1
    else:
        count[pattern] = 1

for (key, value) in count.items():
    if value != 1:
        print(value)