lo=100
up=20000
for num inrange(lo,up+1):
order=len(str(num))
sum=0
temp=num
while temp>0:
digit=temp%10
sum+=digit**order
temp//=10
if num==sum:
print(num)
