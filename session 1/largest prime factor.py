from sympy import primerange 

#num = 13195
#num = 600851475143
num = 81
primes = list(primerange(1, int(num**(1/2))))
#print(primes)

prime_factors = []
quotient = num
i = 0
while quotient>1:
    while(quotient%primes[i]==0):
        quotient/=primes[i]
        prime_factors.append(primes[i])
    i+=1
#print(prime_factors)
print(max(prime_factors))