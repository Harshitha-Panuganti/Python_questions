#check given number is armstrong number or not
number=input()
len_num=len(number)
total=0
for i in number:
    total=total+int(i)**len_num
if total == int(number):
    print('Armstrong Number')
else:
    print('Not an Armstrong Number')