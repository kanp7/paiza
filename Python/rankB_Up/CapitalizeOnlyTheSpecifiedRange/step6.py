# スペース区切りの2つの整数が入力されるので、その区間の全ての整数を順に表示してください。

a,b = map(int,input().split())

for i in range(a, b+1):
    print(i)