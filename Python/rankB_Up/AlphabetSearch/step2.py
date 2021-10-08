# 英大文字の文字列が入力されます。
# この文字列の先頭1文字と末尾1文字で表される範囲に含まれる文字をすべて出力してください。

# 範囲とは、アルファベット順に並べた英大文字の列('A', 'B', 'C', ..., 'Z')について、先頭の文字の出現位置から末尾の文字の出現位置までの部分列のことです。
# たとえば、先頭の文字が'G'で末尾の文字が'O'で表される範囲は、('G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O')となります。

# 出力はアルファベット順に表示し、1文字表示するたびに改行してください。

s = input()

first = ord(s[0])
last = ord(s[-1])

for n in range(first,last+1):
    print(chr(n))

# PythonでUnicodeコードポイント（文字コード）と文字を相互に変換するには組み込み関数chr(), ord()を使う。


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

first = string[0]
last = string[len(string) - 1]

flag = False
for alphabet in alphabets:
    if first == alphabet:
        flag = True

    if flag:
        print(alphabet)

    if last == alphabet:
        break