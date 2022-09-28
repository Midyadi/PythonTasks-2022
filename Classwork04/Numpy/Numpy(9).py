import numpy as np

def is_prime(number):
    k = 0
    for i in range(2,number//2+1):
        if number%i==0:
            k+=1
    return k

def prime_numbers(amount):
    prime_vec = []
    number = 2
    while len(prime_vec)<amount:
        if is_prime(number)==0:
            prime_vec.append(-number)
        number+=1
    return prime_vec
prime_vec = np.array(prime_numbers(10))

def fibonacci_numbers(amount):
    fib_vec = [1,1]
    f1,f2 = 1,1
    for i in range(amount-2):
        f1,f2 = f2, f1+f2
        fib_vec.append(f2)
    return fib_vec
fib_vec = np.array(fibonacci_numbers(10))

skal = prime_vec.dot(fib_vec)
print(skal)


