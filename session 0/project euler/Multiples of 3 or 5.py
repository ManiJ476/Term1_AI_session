num = 1000
list = []
for x in range(1,num):
    if(x%5==0 or x%3==0):
        list.append(x)
#print(list)
print(sum(list))