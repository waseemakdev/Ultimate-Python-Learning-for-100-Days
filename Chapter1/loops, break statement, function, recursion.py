# Loops
#  Loops are used to repeat the values.
#  two types of loops in python.
#  while loop and for loop

# count =1
# while count<=5:
#     print("Helllo World")
#     count+=1


    # break and continue in loops
    # break is used to break the loop and continue is used to skip the current iteration 
    # and move to the next iteration.

# lazz=[2,3,4,5,"Hello","Codie","python"]

# for ax in lazz:
#     print("The List index: ", ax)

# tup=(43,"Hello",3.14,"python",3,4,5)  
# for i in tup:
#     print("The Tuple index: ", i)
    
# Randge in loops
# range is used to generate a sequence of numbers. it can take 3 parameters start, stop and step. by default start is 0 and step is 1.
# 
# for i in range(5): <---------- (only stop parameter)
#     print("The Range index: ", i)

# for i in range(2,11): # <---------- (start and stop parameter)
#     print("The Range index: ", i)

# for i in range(2,11,2): # <---------- (start, stop and step parameter)
#     print("The Range index: ", i)


# Pass Statement in loops
# Pass statement is used to skip the current iteration and move to the next iteration. 
# it is used when we want to write the code later or when we want to skip the iteration for some reason.

# Recursion in python
# Recursion is a function that calls itself. it is used to solve the problems that can be solved by breaking them into smaller subproblems. it is also used to solve the problems that can be solved by using loops.

# def factorial(n):
#     if(n==0) or n==1:
#         return 1
#     return n*factorial(n-1)

# print(factorial(5))    

# print the sum of a natural number

# def cal(n):
#     if (n==0) or n==1:
#         return 1    
#     return n + cal(n-1)

# print(cal(5))    

# print all elements in a list for recursion.



def print_list(list2,n):
    if(n<0):
        return 
    print("Hello from list")
    print(list2[n])
    return print_list(list2, n-1)

list1=[1,2,3,4,5]
print("Hello ")
print_list(list1, len(list1)-1)

# Arithmetic Operation
=> Multiplication 21+5
=> Subtraction 21-5
=> Addition 21*5 
=> Division 21/5
=> Floor Operation 21//5

#Tuple and Functions

# Dictionaries in Python
