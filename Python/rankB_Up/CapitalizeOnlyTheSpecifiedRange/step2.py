# スペース区切りの2つの整数が入力されるので、それらを足して出力してください。

a, b = map(int,input().split())
print(a+b)

# 解答２
std_in = input()
result = 0

for num in std_in.split():
    result += int(num)

print(result)