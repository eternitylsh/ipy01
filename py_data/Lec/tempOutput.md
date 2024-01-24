```python
import random as rd;
```


```python
rd.random() #float x, 0.0 <= x < 1.0.
```




    0.52324739683462




```python
rd.uniform(1, 45) # float x, 0.0 <= x < 45.0
```




    8.628469801521234




```python
rd.randint(1, 45) # 정수 x, 1 <= x < 45 ;; endpoints include.
```




    8




```python
# 함수로 만들어지는 정수 중에 하나를 랜덤하게 리턴.
rd.randrange(0, 101, 2)
```




    10




```python
# 랜덤하게 하나의 원소를 선택.
rd.choice('apple is good') # Choose a random element.
```




    'p'




```python
# 랜덤하게 여러개의 원소를 선택.
rd.sample([1, 2, 3, 4, 5, 6, 7, 8], 4) # choice 4 random elements.
```




    [8, 1, 3, 6]




```python
# 요소를 랜덤하게 섞기
a = [1,2,3,4,5,6,7,8] # shuffle in elements.
print(a)

rd.shuffle(a)
print(a)
```

    [1, 2, 3, 4, 5, 6, 7, 8]
    [6, 7, 2, 3, 1, 4, 8, 5]



```python
lslots = [] # lotto slots : max = 6
max = 6
rint = 0
while True:
    rint = rd.randint(1, 45)
    if rint in lslots:
        continue
    else: 
        lslots.insert(-1, rint)
    
    if max <= len(lslots):
        break

print(lslots)
```

    [8, 19, 16, 23, 1, 44]

