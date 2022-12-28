#find Sum of numbers from M to N
M=int(input())
N=int(input())
sum=0
for i in range(M,N+1):
    sum+=i 
print(sum)