m=int(input())
n=int(input())
count=0
for i in range(m,n+1):
    for j in range(1,i+1):
        if j*j == i:
            count+=1
print(count)