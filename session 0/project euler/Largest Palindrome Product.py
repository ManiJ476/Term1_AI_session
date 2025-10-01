num = 9009
max = 0
for x in range(900,1000):
    for y in range(900,1000):
        num = x*y
        num_str = str(num)
        rev_num = num_str[::-1]
        #print(num_str,rev_num)
        if num_str == rev_num:
            max=num
            factors = (x,y)

print(factors,max)
