def wtf(abc):
    a=set()
    for i in abc:
        if i in a:
            return False
        a.add(i)
    return True

print(wtf("lligma"))
print(wtf("ligma"))

