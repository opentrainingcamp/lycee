#U(0)=2
u=2
L=[]
L.append(u)
print(L)
for i in range(1,5): # range(1,5) c'est l'interval [1 , 5[ 
    u = u + 3 #U(i+1) = U(i) + 3
    L.append(u)
    print(L)
