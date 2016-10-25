import numpy as np

n = int(input())
x = list(map(int, input().split()))

m = np.median(x)

if len(x) % 2 != 0:
	x.remove(m)

a = x[:len(x) // 2]
b = x[len(x) // 2:]

print(int(np.median(a)))
print(int(m))
print(int(np.median(b)))