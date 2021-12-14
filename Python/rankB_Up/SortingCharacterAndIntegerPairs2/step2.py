# 指定された配列（リスト）の定義の中で、同じ値が存在した場合はtrueを、そうでない場合はfalseを出力してください。

array = ["HND", "NRT", "KIX", "NGO", "NGO"]
new_array = []

for a in array:
    if not a in new_array:
        new_array.append(a)
    else:
        print("true")
        break
else:
    print("false")

# 解答2
array = ["HND", "NRT", "KIX", "NGO", "NGO"]
duplicate = False

for i in range(len(array)):
    for j in range(len(array)):
        if i != j and array[i] == array[j]:
            duplicate = True

if duplicate:
    print("true")
else:
    print("false")