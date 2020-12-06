from sys import stdin,stdout
input=stdin.readline
t=int(input())
for _ in range(t):
    s=input()[:-1]
    arr=[]
    top=s[0]
    a=0
    for i in s:
        if i==top:
            a+=1
        else:
            if top=='1':
                arr.append(a)
            a=1
        top=i
    if top == '1':
        arr.append(a)
    arr=sorted(arr,reverse=True)
    ans=0
    for i in range(0,len(arr),2):
        ans+=arr[i]
    print(ans)