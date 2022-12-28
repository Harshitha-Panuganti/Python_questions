n = input()
digit = len(n)
s = 0
if int(n)>=1:
    for i in range(1,int(n)+1):
        count = i
        s = s+len(str(count))
    print(s)    
else:
    print(digit)