st1=input("Enter your stting: ")
c={}
for i in st1:
    if i in c:
        c[i]=c[i]+1
    else:
        c[i]=1
print(c)
