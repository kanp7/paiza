# 0 または 1 の整数 A, B, C, D が与えられます。 以下の式を計算した結果を出力してください。


a,b,c,d = map(int,input().split())
print( int(not( ( (not a) and (not b) ) or (not c) ) ^ d) )
a, b, c, d = map(int, input().split())

# 解答2
a, b, c, d = map(int, input().split())
print(((a or b) and c) ^ d)
# Python でド・モルガンの法則を用いた例です。こちらも簡潔な式となっています。
