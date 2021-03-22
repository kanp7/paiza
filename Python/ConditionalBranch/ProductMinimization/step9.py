# 高さH、幅Wの箱( 0 ≦ H, W ≦ 10^9 )があります。この箱を 1 つ以上の高さ 2 、幅 2 の四角いタイルで敷き詰めます。箱に隙間なくタイルを敷き詰めることはできますか？

h, w = map(int,input().split())


if (h < 2) or (w < 2):
    print("NO")
elif (h % 2 == 0) and (w % 2 == 0):
    print("YES")    
else:
    print("NO")