def print_rangoli(size):
    s=0
    list_1=[]
    col_start=97+size-1
    for i in range(97+size,96,-1):
        list_1.insert(s,[chr(x) for x in range(col_start,i,-1)])
        if s>0:
            list_1[s].extend([chr(x) for x in range(i,size+97)])
        s=s+1
    for j in range(97,size+97):
        list_1.insert(s,[chr(x) for x in range(col_start,j,-1)])
        list_1[s].extend([chr(x) for x in range(j+2,size+97)])
        s=s+1
    lis_2=['-'.join(x) for x in list_1]
    lis_2.pop(0);lis_2.pop(-1)
    for x in lis_2:
        print(x.center(len(lis_2[size-1]),'-'))
