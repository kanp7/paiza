n, x_h, p_h = list(map(int,input().split()))

students = []
for _ in range(n):
    students.append(int(input()))
students += [x_h, p_h]

order_height = sorted(students)
print(order_height.index(p_h)+1)
