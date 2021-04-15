n = int(input())
string = list(input())

# lower-case a-z
alp = [chr(i) for i in range(97,97+26)]
# 下記でもOK
# alp =[chr(ord("a")+i) for i in range(26)]

ans = []
for a in alp:
    count = 0
    for s in string:
        if a == s:
            count += 1
    ans.append(count)
# intをstrに直さないとjoinでうまく結合できない
ans = list(map(str,ans))
print(" ".join(ans))