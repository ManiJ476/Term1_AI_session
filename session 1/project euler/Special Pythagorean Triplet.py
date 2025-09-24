
found = 0
for x in range(1,999):
    for y in range(x+1,1000):
        if(x**2+y**2 == (1000-x-y)**2):
            print(x,y,1000-x-y,'  ',x*y*(1000-x-y))
            found =1
            break
    if found:
        break
   