n=-1
while n<0:
    n=int(input("Saisir n :"))
x=int(input("Saisir x :"))
# Initiliser les variable necessaires
# P va contenir x^i
# et i le conteur
P=1
i=0
# P = x^0
# car x^0 = 1
while i<n:
    i = i+1
    P = P * x
#en sortie de while i == n 
#donc P=x^n
print(P)
    
    