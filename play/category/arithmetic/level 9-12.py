import random

def level_9():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)
    d = random.randint(1, 10)
    
    while c - d == 0:
        c = random.randint(1, 10)
        d = random.randint(1, 10)
    
    print(f"Selesaikan soal berikut: ({a}+{b})/({c}-{d})")
    answer = (a + b) / (c - d)
    return answer

def level_10():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    print(f"Jika a={a}, b={b}, c={c}, tentukan nilai dari a² + b x c!")
    answer = a**2 + b*c
    return answer

def level_11():
    a = random.randint(2, 10)
    b = random.randint(1, a - 1)

    while a - b == 0:
        b = random.randint(1, a - 1)

    print(f"Selesaikan soal berikut: ({a}² - {b}²)/({a} - {b})")
    answer = (a**2 - b**2) / (a - b) 
    return answer

def level_12():
    a = random.randint(1, 5)   
    b = random.randint(1, 5)  
    while a == b:             
        b = random.randint(1, 5)

    c = random.randint(1, 10) 
    d = random.randint(1, 10)  

    print(f"Selesaikan persamaan berikut: {a}x + {c} = {b}x - {d}")
    answer = (c + d) / (b - a)
    return answer