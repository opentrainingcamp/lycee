#U(0)=2
u=2
v=1
L1=[]
L2=[]
L1.append(u)
L2.append(v)
print(L1)
print(L2)
for i in range(4):  
    u = u + 3
    v = v + 5
    L1.append(u)
    L2.append(v)
print("suite u L1=",L1)
print("suite v L2=", L2)
print("Concaténation des 2 liste L2,L1 =",L2+L1)
print("cette fois ci triée" , sorted(L2+L1))

