# スペース区切りで2つの整数が入力されるので、その区間の整数を全て表示してください。


a,b = list(map(int,input().split()))

for n in range(a, b+1):
    print(n)