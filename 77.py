num=input('enter a number');
if num=='x':
exit();
else:
count=0;
number=int(num);
for i in range(2,number-1):
if number%i==0:
print(i);
i+=1;
count+=1;
if count==0:
print(' ')
print(number,'is a prime number')
