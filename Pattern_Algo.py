import time
n,m=map(int,input().split())
w="WELCOME"
for i in range(1,(n//2)+1):
    time.sleep(1)
    print("-"*((m-3*(2*i-1))//2)+".|."*(2*i-1)+"-"*((m-3*(2*i-1))//2))
time.sleep(1)
print("-"*((m-len(w))//2)+w+"-"*((m-len(w))//2))
j=n//2
for i in range(1,(n//2)+1):
    time.sleep(1)
    print("-"*((m-3*(2*j-1))//2)+".|."*(2*j-1)+"-"*((m-3*(2*j-1))//2))
    j-=1
