# 文字列がスペース区切りで２つ入力されるので、スペースで分割し、2行で出力してください。


a, b = input().split()
print(a)
print(b)

# 解答２
std_in = input()

for string in std_in.split():
    print(string)