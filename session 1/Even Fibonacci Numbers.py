series = [1,2]
i = 2
x = 0
while (1):
    x=series[i-1]+series[i-2]
    if(x>4000000):
        break
    series.append(x)
    i+=1

even_sum=sum([x for x in series if x%2==0])
print(even_sum)