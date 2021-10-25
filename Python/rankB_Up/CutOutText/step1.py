# 文字列がスペース区切りで2つ入力されるので、スペースで分割し、2行で出力してください。

a,b = input().split()
print(a)
print(b)

# 解答2
std_in = input()

for string in std_in.split():
    print(string)