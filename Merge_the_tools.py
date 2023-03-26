def merge_the_tools(string, k):

    n=len(string)
    list_1=[]
    list_2=[]
    for i in range(0,n,k):
        list_1.append(string[i:i+k])


    for x in list_1:
        new_str=""
        for j in range(0,k):
            if x[j] in x[:j]:
                continue
            else:
               new_str=new_str+x[j]
        list_2.append(new_str)

    for y in list_2:
        
        print(y)
