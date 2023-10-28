import random

def bub(array):
    for i in range(n-1):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


a = input("Enter size: ")
n, m = a.split(" ")
n = int(n)
m = int(m)

A = []
for i in range(n):
    A.append([0] * m)

for i in range(n):
    for j in range(m):
        A[i][j] = random.uniform(-100, 100)

print()

for i in range(n):
    for j in range(m):
        print("%4d " % (int(A[i][j])), end=' ')
    print()

print()

B = [0] * n

for i in range(n):
    for j in range(m):
        if j == i:
            B[i] = A[i][j]

bub(B)

for i in range(n):
    for j in range(m):
        if j == i:
            A[i][j] = B[i]

for i in range(n):
    for j in range(m):
        print("%4d " % (int(A[i][j])), end=' ')
    print()
