#U(0)=2
n=5
u=2
print(u)
while n>0: # on rentre dans la boucle si n>0 on sort donc quand n<=0
    u = u + 3 #U(i+1) = U(i) + 3
    n = n - 1
    print(u)
