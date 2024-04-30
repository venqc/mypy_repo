
# class Square:
# 	def __init__(self, side):
# 		""" creates a square having the given side
# 		"""
# 		self.side = side

# 	def area(self):
# 		""" returns area of the square
# 		"""
# 		return self.side**2

# 	def perimeter(self):
# 		""" returns perimeter of the square
# 		"""
# 		return 4 * self.side

# 	def __repr__(self):
# 		""" declares how a Square object should be printed
# 		"""
# 		s = 'Square with side = ' + str(self.side) + '\n' + \
# 		'Area = ' + str(self.area()) + '\n' + \
# 		'Perimeter = ' + str(self.perimeter())
# 		return s


# if __name__ == '__main__':
# 	# read input from the user
# 	side = int(input('enter the side length to create a Square: '))
	
# 	# create a square with the provided side
# 	square = Square(side)

# 	# print the created square
# 	print(square)
#------------------------------------------------------
# num = 21
# # If given number is greater than 1
# if num > 1:
#     # Iterate from 2 to n // 2
#     for i in range(2, (num//2)+1):
#         # If num is divisible by any number between
#         # 2 and n / 2, it is not prime
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")


#-----------------------------------------
# #basic flag method
# for num in range(2,101):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False
#     if prime:
#        print (num)
#--------------------------------------
# for num in range(2,26):
#     if all(num%i!=0 for i in range(2,num)):
#        print (num)
# --------------------------------------------
# for num in range(2,101):
#     prime = True
#     for i in range(2,num**0.5):
#         if (num%i==0):
#             prime = False
#     if prime:
#        print (num)

# import math
# print (2)
# for num in range(3,26,2):
#     if all(num%i!=0 for i in range(3,int(math.sqrt(num))+1, 2)):
#         print (num)

# --------------------------------------------
# x = int(input('Enter x value: '))
# # Explain the below code line by line
# for num in range(2, x):
#     prime = True
#     for i in range(2,num):
#         if (num%i==0):
#             prime = False 


#     if prime:
#        print (num)

#Explain below code:

# num = 2
# if num > 1:
#     for i in range(2, (num//2)+1):
#         if (num % i) == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

