num = 100

sum_of_squares=0
for x in range(1,num+1):
    sum_of_squares+= x**2
#print(sum_of_squares)

square_of_sum = sum(range(1,num+1))**2
#print(square_of_sum)

print(square_of_sum-sum_of_squares)