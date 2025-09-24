from sympy import primerange 
import numpy as np


num = 20
primes = list(primerange(1, int(num)))
#print(primes)

max_powers=np.zeros(len(primes))
for x in range(1,num+1):
    quotient = x
    i = 0
    while quotient>1:
        count=0
        while(quotient%primes[i]==0):
            quotient/=primes[i]
            count +=1
        if(count>max_powers[i]):
            max_powers[i]=count
        i+=1
#print(max_powers)

product=1
for i in range(len(primes)):
    product *= primes[i]**max_powers[i]
print(product)