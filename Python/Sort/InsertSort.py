def insertion_sort(a, n):
    for i in range(1, n):
        x = a[i] 
        j = i-1 

        while j >= 0 and a[j] > x:
            a[j+1] = a[j]
            print(a)
            j -= 1
        
        a[j+1] = x

        print(*a)


n = int(input())
# 5
a = list(map(int, input().split()))
# [4, 1, 3, 5, 2]

insertion_sort(a, n)