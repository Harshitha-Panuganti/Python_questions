n=int(input())
term_number="1"
term=0
for i in range(1,n+1):
    c=(term_number)*i
    term=term+int(c)
print(term)