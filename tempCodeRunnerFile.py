arr=[]
while(True):
    num=int(input())
    if(num>0):
        arr.append(num)
    else:
        break

for i in range(len(arr)-1):
    if(arr[i]<10 and arr[i+1]<10):
        arr.remove(arr[i])
        i-=1
print(arr)