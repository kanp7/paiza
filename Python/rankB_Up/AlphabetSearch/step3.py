# 英大文字の文字列が入力されます。
# 文字列の先頭1文字が、末尾1文字よりもアルファベット順で先に出現するならば、"true"を出力し、そうでなければ"false"を出力してください。

s = input()
if s[0] < s[-1]:
    print("true")
else:
    print("false")


# Python3では文字列strはUnicodeであり、文字列の大小関係（順番）は文字のUnicodeコードポイント（文字コード）で判定される。


# 解答2
string = input()
alphabets = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
result = "true"

first = string[0]
last = string[len(string) - 1]

for alphabet in alphabets:
    if first == alphabet:
        break

    if last == alphabet:
        result = "false"

print(result)