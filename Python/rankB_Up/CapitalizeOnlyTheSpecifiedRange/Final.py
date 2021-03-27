# スペース区切りの2つの整数と、文字列が入力されます。2つの整数の範囲の部分文字列を、大文字にして出力してください。

a, b = map(int, input().split())
s = input()

count = 0
str = []
for i in s:
    count += 1
    if count > a-1 and count < b+1:
        str.append(i.upper())
    else:
        str.append(i)

print("".join(str))