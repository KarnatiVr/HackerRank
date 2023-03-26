D=input()
n,m=map(int,D.split())
H=".|."
k=0
for i in range(n//2):
    k=k+1
    print((H*(i+k)).center(m,'-'))
    
print("WELCOME".center(m,'-'))
for i in range(n//2,0,-1):
    k=k-1
    print((H*(i+k)).center(m,'-'))
