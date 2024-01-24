import random as rd
import time

def Gen_L6list():
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
            return lslots
    # fail result : -1
    return -1

def L6_Check(cycle):
    str = '■'
    per = cycle // 100
    for i in range(cycle):
        sample = Gen_L6list()
        count = 0
        pr = (i+1) // per
        for e in sample:
            for c in sample:
                if e == c:
                    count += 1
            if 1 < count:
                print('\n')
                print(f'중복값 발견 : loop_idx: {i}, target sample : {sample}, target value : {e}')
                return False
            count = 0
        print(f'{pr:<3}% >>> |{str * (pr // 2):<50}|', end='\r')
        # time.sleep(0.001) # 그냥 쓸데없이 집어넣음.
    print('\n')
    return True
cycle = int(input('check count : ') or 10000)
print( 'All Clear.' if L6_Check(cycle) else 'Fail Error;;' )