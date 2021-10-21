# a ~ z のアルファベットを、改行区切りで出力してください。


alp = ([chr(i) for i in range(97,97+26)])
# alp = ([chr(ord("a")+i) for i in range(26)])

for n in alp:
    print(n)