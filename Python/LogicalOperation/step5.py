# A NAND B の結果を 0 または 1 で出力してください。末尾に改行を入れ、余計な文字、空行を含んではいけません。

a, b = map(int,input().split())

print(int(not (a and b)))

# NAND 演算は NOT AND 演算の略で、論理積の否定となります。
# 多くの言語において NAND を表現する二項演算子は定義されていませんが、 ド・モルガンの法則 という法則を用いると、これまでに学習した OR, NOT 演算を組み合わせることによって NAND 演算と等価な演算を実現することが可能です。ド・モルガンの法則とは、以下の等式が成り立つ法則です。
# NOT(X AND Y) = NOT(X) OR NOT(Y)
# NOT(X OR Y) = NOT(X) AND NOT(Y)
