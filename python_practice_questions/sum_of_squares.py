# Sum of squares of the first natural numbers
m=int(input())
sum=0
for i in range(1,m+1):
    sum = sum + (i*i)
print(sum)

#sum of cubes of the first natural numbers
number = int(input())
total = 0
for i in range(1,number+1):
    total = total + i**3
print(total)