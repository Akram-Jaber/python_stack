for i in range (0,151,1):
    print(i)

for i in range (0,1001,5):
    print(i)

for i in range (0,101,1):
    if(i%10==0):
        print("cooding dojo")
    elif(i%5==0):
        print("cooding ")
sum=0

for i in range(0,500001,1):
    if(i%2!=0):
        sum=sum+i
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum=2
highNum=9
mult=3
for i in range (lowNum,highNum+1):
    if i % mult ==0:
        print(i)