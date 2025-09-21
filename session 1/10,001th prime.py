num = 10001

primes=[]
x = 2
while(len(primes)<num-1):
    is_prime = 1
    i = 2
    while (i<x/i+1):
        if(x%i == 0):
            is_prime=0
            break
        i+=1
    if(is_prime):
        primes.append(x)
    x+=1
#print(primes)
print(primes[num-2])