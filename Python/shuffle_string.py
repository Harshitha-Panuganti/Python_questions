word=input()
len_word=len(word)
shuffled=""
for i in range(0,len_word):
    n=int(input())
    shuffled = shuffled + word[n]
print(shuffled)