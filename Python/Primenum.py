# write given number prime or not
n=int(input())
for i in range(2,n):
    if(n%i) == 0:
        print('Not a Prime Number')
        break
else:
    print('Prime Number')

