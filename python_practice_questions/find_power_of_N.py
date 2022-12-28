#Given integer N,and exponent M as input write a program N power of M
#without using power operator (**)
N=int(input())
M=int(input())
product=1
count=0
while count < M:
    product = product * N 
    count=count+1
print(product)