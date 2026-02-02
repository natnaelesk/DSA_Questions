ln = int(input())
s = input()
arr = list(map(int , s.split()))
Sereja ,Dima = 0,0



i =0
while arr:
    if i%2==0:
        if arr[0] > arr[-1]:
            Sereja +=arr[0]
            arr.pop(0)
        else:
            Sereja +=arr[-1]
            arr.pop()
    else:
        if arr[0] > arr[-1]:
            Dima +=arr[0]
            arr.pop(0)
        else:
            Dima +=arr[-1]
            arr.pop()
    i+=1
        
        


print(Sereja , Dima )