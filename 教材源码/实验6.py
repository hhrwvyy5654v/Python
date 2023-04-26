from random import randint

def isPrime(n):
    if n in (2,3):
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i==0:
            return False
    return True

lst = [randint(1,100) for _ in range(50)]
print(lst)
print(list(filter(lambda n:isPrime(n) is False, lst)))
