# paiza 君のクラスには paiza 君を含めて N + 1 人の生徒がいます。paiza 君の身長は P cm です。paiza 君以外の N 人の生徒の身長は A_1, ... ,A_N です。
# 今日、クラスに身長 X cm の転校生が 1 人やってきました。転校生が入ってきた後 N + 2 人のクラス全員で背の順で並んだ時、 paiza 君は前から何番目に並ぶことになるでしょうか。

# なお、背の順の先頭の生徒を前から 1 番目の生徒とします。

n, x_h, p_h = list(map(int,input().split()))

students = []
for _ in range(n):
    students.append(int(input()))
students += [x_h, p_h]

order_height = sorted(students)
print(order_height.index(p_h)+1)
