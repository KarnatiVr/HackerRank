if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    M=0
    s=[]
    for i in range(0,x+1):
        for j in range(0,y+1):
            for k in range(0,z+1):
                s.insert(M,[i,j,k])
                M=M+1
    N=list(filter(lambda x:((x[0]+x[1]+x[2])!=n), s))
    print(N)
