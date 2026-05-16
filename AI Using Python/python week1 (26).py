# Lamba function---written in  a single line
add= lambda a,b:a+b
print(add(8765,985746))

double_it= lambda n:n*9
print(double_it(76767))

nums=[1,2,3,4]
squares= list(map(lambda x:x*x,nums))
print(squares)

numbers=[1,2,3,4,5,6,7,8,9,10]
odd_numbers=list(filter(lambda x:x%2 !=0,numbers))
print(odd_numbers)