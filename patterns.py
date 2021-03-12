#patterns
#1st pattern program---------------------
n=5
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(" ",end="")
    k=k-2
    for j in range(0,i+1):
        print("* ",end="")
    print("\r")
 

#2nd pattern program---------------------
n=5
av=65
for i in range(0,n):
    for j in range(0,i+1):
        ch=chr(av)
        print(ch,end=" ")
        av=av+1
    print("\r")
