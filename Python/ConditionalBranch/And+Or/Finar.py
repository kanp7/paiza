# 3 つの整数X, Y, Zが与えられます。「Xが 10 以上」かつ「Yが 10 以上」の場合はYESを、そうではない場合はNOを出力してください。
# ただし、「Zが 10 以上の」場合はXとYの値にかかわらず、必ずYESを出力してください。

x,y,z = map(int,input().split())

if z >= 10:
    print("YES")
elif x >= 10 and y >= 10:
    print("YES")
else:
    print("NO")