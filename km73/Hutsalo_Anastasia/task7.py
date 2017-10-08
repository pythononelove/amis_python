N=int(input())
K=N//60
if K>23:
  K-=23
print(int(K))
print(int(N%60))
