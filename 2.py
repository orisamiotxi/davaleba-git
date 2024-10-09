def wtf(abc):
    f={}
    for i in abc:
        if i in f:
            f[i]+=1 
        else:
            f[i]=1 
    return f

print(wtf("LIGGMA BALLS"))
