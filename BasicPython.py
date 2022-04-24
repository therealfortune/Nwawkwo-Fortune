# ages = []
# user_input = int(input('Enter class age , type -1 to quit :>'))

# while user_input > 0:
#     ages.append(user_input)
#     user_input = int(input("Enter next age :> "))
# print(f'There are {len(ages)} age(s) which are {ages}')


# class_names = []
# count = 0
# name = str(input('Enter name of class members , type n to quit :> '))

# while name != 'n' :
#     count += 1
#     class_names.append(name)
#     name = str(input('Enter next name :> '))
# print(f'There are {count} name(s) which are {class_names}')


# n = 100

# for i in range(1, n+1):
#     if i%3 == 0 and i % 5 == 0:
#         print(i, 'FizzBuzz')
#     elif i % 5 == 0:
#         print(i,'Buzz')
#     elif i % 3 == 0:
#         print(i,'Fizz')
#     else:
#         print(i)



# num_1 = int(input('Enter your first numer :> '))
# num_2 = int(input('Enter your second number :> '))


# if num_1 > num_2 :
#     for i in range(num_2, num_1 + 1):
#         print(i)
# elif num_2 > num_1:
#     for n in range(num_1, num_2 + 1):
#         print(n)
# elif num_1 == num_2:
#     print('Equal')
# else:
#     print('Incorrect entry')



    
# num_1 = int(input('Enter first number :> '))
# num_2 = int(input('Enter second number :> '))

# while num_1 < 0 or  num_1 > 101 or num_2 < 0 or num_2 >101:
#     print('Numbers shold be between the range of 1 and 100')
#     num_1 = int(input('Enter first number :> '))
#     num_2 = int(input('Enter second number :> '))
    
# if num_1 > num_2:
#     for i in range(num_2, num_1 + 1):
#         print(i, end=' ')
# elif num_2 > num_1:
#     for j in range(num_1, num_2 + 1):
#         print(j, end=' ')
# elif num_1 == num_2:
#     print("No range , both numbers hold the same value")


## Reverse a string

# user_input = input('Enter a word :> ')
# reverse_string = ""

# for char in user_input:
#     reverse_string = char + reverse_string
# print(reverse_string)

# print(user_input[::-1])


# Multiplication table
# num = input('Enter number :> ')

# while (not num.isnumeric()) or (int(num) < 1 or int(num) > 12):
#     print('Enter a numeric value between the range of 1 and 12 ')
#     num = input('Enter another number :> ')
# num = int(num)
# print()
# print('################')
# print(f'This is the {num} times table')
# print()

# for i in range(1,13):
#     print(num, 'x', i, '=', num*i)


# for i in range(1,13):
#     print()
#     print('Multiplication Table')
#     print('#################')
#     print(f'This is the {i} times table')
#     print()
#     for j in range(1,13):
#         print(i, 'x' ,j, '=', i*j)
    

# marks = []
# num = input('Enter a number :> ')

# while num != 'exit':
#     while not num.isdigit():
#         print('Enter a valid number')
#         num = input('Try again :> ')
#     marks.append(int(num))
#     num = input('Enter next number , type exit to exit :> ')

# sum = 0
# for i in marks:
#     sum += i

# print(f'The average mak of the {len(marks)} numbers is {sum/len(marks)}')
        
    
# n = int(input('Enter a number :> '))
# fact = 1

# for i in range(1, n+1):
#     fact *= i
# print(fact)


# Fibonacci sequence

# n = int(input('Enter a range e.g 20 :>'))
# a = int(input('Enter starting num :>'))
# b = a + 1
# fib_num = []

# for i in range(n):
#     fib_num.append(a)
#     a,b = b, a+b
    
# print(fib_num)


# star = '*'

# for i in range(1,7):
#     for j in range(1,6):
#         if i == 1 and j < 8:
#             print(star, end='')
#         elif i == 2 and j == 1:
#             print()
#             print(star)
#         elif i == 3 and j < 5:
#             print(star, end='')
#         elif i == 4 and j == 1:
#             print()
#             print(star)
#         elif i == 5 and j ==1:
#             print(star)
#         elif i == 6 and j == 1:
#             print(star)



# n = 100

# evens = []
# odds = []

# for i in range(1, n+1):
#     if i%2:
#         evens.append(i)
#     else:
#         odds.append(i)
        
# print(f'This are the even numbers -- {evens}')
# print(f'This are the odds numbers -- {odds}')










































    


















