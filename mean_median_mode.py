from numpy import mean, median
from scipy import stats

n = int(input())
x = list(map(int, input().split()))

print(mean(x))
print(median(x))
print(int(stats.mode(x)[0]))