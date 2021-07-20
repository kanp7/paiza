# ・1行目では整数aが与えられます。aが0より大きいなら"plus"、そうでなければそのまま1行目で表示してください。
# ・2行目では文字列bが与えられます。bが"hoge"に一致するなら"yes"、そうでなければそのまま2行目で表示してください。
# ・3行目では文字列cが与えられます。cが10文字なら"ten"、そうでなければそのまま3行目で表示してください。
# ・4行目では文字列dが与えられます。dが文字"x"を含むなら"x"が最初に見つかった位置、そうでなければ"nothing"を4行目で表示してください。
# ・5行目では文字列eが与えられます。eが5文字なら"five"、そうでなければeの最初の1文字だけを5行目で表示してください。


a = int(input())
print("plus") if a > 0 else print(a)

b = input()
print("yes") if b == "hoge" else print(b)

c = input()
print("ten") if len(c) == 10 else print(c)

d = input()
print(d.index("x")) if "x" in d else print("nothing")

e = input()
print("five") if len(e) == 5 else print(e[0])

# print()のカッコでくくれる
a = int(input())
print("plus" if a >= 0 else a)

b = input()
print("yes" if b == "hoge" else b)

c = input()
print("ten" if len(c) == 10 else c)

d = list(input())
print(d.index("x") if "x" in d else "nothing")

e = input()
print("five" if len(e) == 5 else e[0])