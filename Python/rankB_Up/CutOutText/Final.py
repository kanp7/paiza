# スペース区切りの2つの整数と、文字列が入力されるので、2つの整数の範囲の部分文字列を出力してください。

a, b = map(int, input().split())
s = input()

print(s[a-1:b])