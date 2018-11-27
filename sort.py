import numpy as np

def insertionsort(n):
    a = np.random.randint(0, 100, n)
    print(a)
    for i in range(len(a)):
        j = i - 1
        key = a[i]
        while a[j] > key and j >= 0:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a

new_arr = insertionsort(10)
print(new_arr)





