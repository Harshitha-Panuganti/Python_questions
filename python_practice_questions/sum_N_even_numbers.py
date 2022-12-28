#Find Sum Even numbers in the first natural numbers
n=int(input())
sum=0
for i in range(1,n+1):
    if(i%2 == 0):
        sum+=i
print(sum)

#sum of even numbers from M to N
M=int(input())
N=int(input())
sum=0
for i in range(M,N+1):
    if(i%2 == 0):
        sum+= i 
print(sum)