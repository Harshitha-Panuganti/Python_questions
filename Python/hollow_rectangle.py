m=int(input())
n=int(input())
star_line='* '*n
print(star_line)
for i in range(m-2):
    hollow_spaces = "  "*(n-2)
    star='* ' + hollow_spaces + '* '
    print(star)
print(star_line)