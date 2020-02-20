#U(0)=2
u=2
L=[]
L.append(u)
print(L)
for i in range(4): # range(0,4) c'est l'interval [0 , 4[ 
    u = u + 3 #U(i+1) = U(i) + 3
    L.append(u)
print(L)
print(len(L))
print(L[2])
