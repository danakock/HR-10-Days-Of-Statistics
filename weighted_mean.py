import numpy as np

n = int(input())
x = list(map(int, input().split()))
w = list(map(int, input().split()))

print(np.average(x, weights=w))