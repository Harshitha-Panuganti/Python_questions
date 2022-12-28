#Find Sum Odd numbers in the first natural numbers
n=int(input())
sum=0
for i in range(1,n+1):
    if(i%2 == 1):
        sum+=i
print(sum)


#sum of odd numbers from M to N
m = int(input())
n = int(input())
total = 0
for i in range(m,n+1):
    if (i % 2) ==1:
        total = total + i
print(total)