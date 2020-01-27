```python
def P(U,V):
    return sum(x*y for x,y in zip(U,V))
```


```python
def O(U,V):
    if P(U,V) == 0:
        return "oui"
    else:
        return "non"
```


```python
v1=[1,3]
v2=[22,-5]
```


```python
print(P(v1,v2))
```

    7



```python
v1=[15/22,3]
```


```python
v1
```




    [0.6818181818181818, 3]




```python
print(P(v1,v2))
```

    -1.7763568394002505e-15



```python
print(O(v1,v2))
```

    non



```python
from fractions import Fraction as frac
```


```python
frac(2/5)
```




    Fraction(3602879701896397, 9007199254740992)




```python
frac(2, 5)*5
```




    Fraction(2, 1)




```python
v1=[frac(15,22), 3]
```


```python
print(O(v1,v2))
```

    oui



```python
frac(15,22)
```




    Fraction(15, 22)




```python
print(frac(15,22))
```

    15/22



```python

```
