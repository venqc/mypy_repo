#Tuples
# t1=()
# print(t1)
# print(type(t1))

# t2 = ("hello", )
# t2
# print(t2)

# t3 = ("hello") # No tuple - single element
# print(t3)

# t4 = (1, 5, 20, "python", "hello", True)
# print(t4)
# print(len(t4))

# print(t4[3])
# print(t4[-1])

# t5 = ("hello", 1, 6, 24, 84)
# t6 = "hello", 1, 6, 24, 84 # REMEMBER
# print(type(t5))
# print(type(t6))
# -----------------------------------------------
# t7 = (1, 56, 13, 'python', 'hello')
# # t7[1] = 65 #Tuples are IMMUTABLE # REMEMBER
# #Can only delete entire tuple but not single element like lists
# del t7
# print(t7)
# -----------------------------------------------------
# No, it is not always required to use the “print” statement for displaying datatypes in Jupyter. 
# In Python, you can use the “type()” function to directly print the datatype of a variable.

# Tuples have only count and index, as they are immutable
# -----------------------------------------------------
# t7 = (1, 56, 56, 56, 13, 'python', 'hello')
# print(t7.count(56))
# print(t7.index(56))

# t8 = tuple("python") # Convert string to tuple - tuple constructor #REMEMBER
# print(t8)
# t9 = tuple([8, 5, 91, 125, 'hello'])
# print(t9)

# t10 = t8+t9 # Tuple addition
# print(t10)

t11 = (1, 5, 10, 15, 75, 111,)
t12=t11*3
# print(t11)
# print(t12)

# # t13 = t11*t12 # Tuple - didn't work
# # print(t13)
# print(t12[6:11])
if 111 in t12:
    print(bool())


# -----------------------------------------------------










