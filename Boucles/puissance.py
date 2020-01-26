n=-1
while n<0:
    n=int(input("Saisir n "))
x=int(input("Saisir x "))

# x^n =  (x^(n-1))*x

#initialisaton
P=1 # car x^0 ==1
while n>0:
    P=P*x
    n=n-1
# la la sortie n == 0 donc le calcul est fini
print(P)