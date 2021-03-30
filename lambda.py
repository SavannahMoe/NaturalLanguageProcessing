#lambda allows us to declare anonymous functions 
#an anonymous function refer to a function declared with no name 
#lambda functions can only have a single expression 
#lambda funciton returns a funciton object 

#traditional way of defining function
''' 
def remainder(num):
    return num % 2
'''

#lambda 
remainder = lambda num: num % 2
print(remainder(5))

product = lambda x,y :x*y
print(product(2,3))

#practice 
def testfunc(num):
    return lambda x : x * num 

#result1 = lambda x: x * 10    this is essentialy doing this but not having to create it twice 
#result2 = lambda x: x * 100

result1 = testfunc(10)          #result1 and result2 are lambda funcitons 
result2 = testfunc(100)

print(result1(9))
print(result2(9))


#FILTER FUNCTION 
#filter(object, iterable)

numbers_list = [2, 6, 8, 10, 11, 4, 12, 7, 13, 17, 0, 3, 21]
filtered_list = list(filter(lambda num: (num>7), numbers_list))
print(filtered_list)


#returning double of n 
def addition(n):
    return n + n 

#we double all numbers using regular function 

numbers = (1,2,3,4)
result = map(addition, numbers)
print(list(result))

numbers = [1,2,3,4]
result = list(map(lambda n: n + n, numbers))
print(result)

numbers = [1,2,3,4]
numbers2 = [5,6,7,8]
result = list(map(lambda x, y: x + y, numbers, numbers2))
print(result)