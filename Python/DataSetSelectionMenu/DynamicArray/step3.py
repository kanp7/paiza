# 自然数A, B, Cが与えられます。(A, B, Cの最大値) - (A, B, Cの最小値)を答えてください。

lists = list(map(int,input().split()))
print(max(lists)-min(lists))