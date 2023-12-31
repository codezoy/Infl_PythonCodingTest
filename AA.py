import sys
sys.stdin = open('input.txt', 'rt')
# Question: std.stdin이 뭐야?
# 
# n = input()
N, K = map(int, input().split(' '))

divisor = []
i = 1
for i in range(1, N+1):
    if N%i==0:
        divisor.append(i)

if len(divisor)<K:
    print("-1")
else:
    print(divisor[K-1])