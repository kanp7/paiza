# 要素数Nの数列Aと数値Mが与えられます。AのM番目の値を出力してください。

n,m = map(int,input().split())
lists = list(map(int,input().split()))
print(lists[m-1])