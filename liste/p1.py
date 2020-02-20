#U(0)=2
u=2
print(u)
for i in range(1,5): # range(1,5) c'est l'interval [1 , 5[ 
    u = u + 3 #U(i+1) = U(i) + 3
    print(u)

### une autre on imprime i et u
#U(0)=2
u=2
print(0, u)
for i in range(1,5): # range(1,5) c'est l'interval [1 , 5[ 
    u=u+3 #U(i+1) = U(i) + 3
    print(i,u)