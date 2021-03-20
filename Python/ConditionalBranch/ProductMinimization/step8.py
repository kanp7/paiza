# 直線上の道があり、最初は X = 0 の地点にいます。この道はX = T + 0.1 の地点で崖になっています。また、 1 歩でX軸方向にK進むことができます。崖に落ちずにN歩進むことはできるでしょうか。

n,k,t = map(int,input().split())

if n*k > t:
    print("NO")
else:
    print("YES")