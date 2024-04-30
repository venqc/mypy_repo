#Loops
#Main Section

n = int(input("Enter n\'s value: "))
def basic_loops():
    for i in range(n):
        for j in range(n):
            print('*', end='')

# print(basic_loops())
basic_loops()
#---------------------------------
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(n):
#             print('*', end='')
#         print() # Vimp

# # print(basic_loops())
# basic_loops()
# ---------------------------------
n = int(input('Enter n\'s value: '))
def basic_loops():
    for i in range(n):
        for j in range(i+1):
            print('*', end='')
        print() # Vimp

# print(basic_loops())
basic_loops()
#-----------------------------------
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(5-i):
#             print('*', end='')
#         print() # Vimp

# # print(basic_loops())
# basic_loops()
#-----------------------------------------
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(i, n): #range(start, stop, step)
#             print('*', end='')
#         print() # Vimp

# # print(basic_loops())
# basic_loops()
#-----------------------------------------
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(i, n): #range(start, stop, step)
#             print(' ', end='')
#         for j in range(i+1):
#             print('*', end='')
#         print() # Vimp

# # print(basic_loops())
# basic_loops()
#-----------------------------------------
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(i, n): 
#             print('*', end='')
#         for j in range(i+1):
#             print('#', end='')
#         print() # Vimp

# # print(basic_loops())
# basic_loops()
# ----------------------------------------------
# def basic_loops():
#     for i in range(5):
#         for j in range(i, 5): 
#             print(' ', end='')
#         for j in range(i+1):
#             print('*', end='')
#         print() # Vimp
# basic_loops()
#----------------------------------------
# Hill
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(i, n): 
#             print(' ', end='')
#         for j in range(i+1):
#             print('*', end='')
#         for j in range(i):
#             print('*', end='')

#         print() # Vimp
# basic_loops()
#----------------------------------------
# Inverted Hill
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(i+1): 
#             print(' ', end='')
#         for j in range(i, n-1):
#             print('*', end='')
#         for j in range(i, n):
#             print('*', end='')

#         print() # Vimp
# basic_loops()
#----------------------------------------
#Diamond
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n-1):
#         for j in range(i, n): 
#             print(' ', end=' ')
#         for j in range(i+1):
#             print('*', end=' ')
#         for j in range(i):
#             print('*', end=' ')
#         print() # Vimp

#     for i in range(n):
#         for j in range(i+1): 
#             print(' ', end=' ')
#         for j in range(i, n):
#             print('*', end=' ')
#         for j in range(i, n-1):
#             print('*', end=' ')
#         print() # Vimp
# basic_loops()
#------------------
# n = int(input('Enter n\'s value: '))
# def basic_loops():
#     for i in range(n):
#         for j in range(i, n): 
#             print(n-i, end=' ')
        
#         print()
# basic_loops()
#-----------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(n):
#             if i==0 or j==0 or i==n-1 or j==n-1: 
#                 print('#', end=' ')
#             else:
#                 print(' ', end=' ')            
#         print()
# hollow_patterns()
#-------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(n):
#             if (j == 0 or j == n-1):    
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')     
#         print()
# hollow_patterns()
#-----------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(n):
#             if (i == n // 2 or j == n // 2):    
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')     
#         print()
# hollow_patterns()
#-----------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(n):
#             if (i == j or i+j == n-1):    
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')     
#         print()
# hollow_patterns()
#-----------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(i+1):
#             if i==n-1 or i==j or j ==0:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
                  
#         print()
# hollow_patterns()
#-----------------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(i, n):
#             if i == 0 or j == i or j == n-1:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
                  
#         print()
# hollow_patterns()
#-----------------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(i, n):
#             if i == 0 or j == i or j == n-1:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         for j in range(i+1):
#             if i == n-1 or j == i or j == 0:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
                  
#         print()
# hollow_patterns()
# ------------------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n):
#         for j in range(i, n):
#                 print(' ', end=' ')
#         for j in range(i):
#             if i == n-1 or j == 0:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         for j in range(i+1):
#             if i == n-1 or j == i:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')                 
#         print()
# hollow_patterns()
# ------------------------------------------------------------
# n = int(input("Enter the value of n: "))
# def hollow_patterns():
#     for i in range(n-1):
#         for j in range(i, n-1):
#                 print(' ', end=' ')
#         for j in range(i):
#             if j == 0 :
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         for j in range(i+1):
#             if j == i:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')                 
#         print()

#     for i in range(n):
#         for j in range(i):
#                 print(' ', end=' ')
#         for j in range(i, n):
#             if j == i:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         for j in range(i, n-1):
#             if j == n-2:
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')                 
#         print()
# hollow_patterns()
# --------------------------------------------------------
# Print hollow diamond

# n = int(input("Enter grid size n: "))
# def hollow_diamond():
#     for i in range(n-1):
#         for j in range(i+1):
#             if i== 0 or i== (n-1) or j ==(int(n/2)):
#                 print('*', end=' ')
#             elif i == (i+1) or j == ((int(n/2))+i) or j == ((int(n/2))-i):
#                 print('*', end=' ')
#             else:
#                 print(' ', end=' ')
#         print()
# hollow_diamond()
#----------------------------------------------------------------
# def print_pattern(n):
#     # Upper half
#     for i in range(n):
#         print(" " * (n - i - 1) + "*" + " " * (2 * i) + "*")
#     # Lower half
#     for i in range(n - 2, -1, -1):
#         print(" " * (n - i - 1) + "*" + " " * (2 * i) + "*")
# # Define the number of rows (adjust as needed)

# print_pattern(5)
#help(range) 
#--------------------------------------------------------------
n = int(input("Enter grid size n: "))
def print_pattern():
   for i in range(n):
     for j in range(n):
        print('*', end=' ')
     print()       
print_pattern()
   