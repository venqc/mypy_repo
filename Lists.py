#Lists: Organize your data so you can work with it efficiently.
#lists among lists, sets, dictionaries, and tuples
# flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
# print(type(flowers))
# print(flowers)
# flowers = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
# print(type(flowers))
# print(flowers)
# print(len(flowers))
# print(flowers[3])
# print(flowers[0])
# print(flowers[1],[5])
# print(flowers[1],flowers[5])
# print("First entry with 0 index is: " + flowers[0])
# print("First entry with 0 index is: ", flowers[0])
# -----------------------------------------------------
# Slicing
# -----------------------------------------------------
# flowers_list = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells", "sweet pea", "english marigold", "tiger lily", "moon orchid", "bird of paradise", "monkshood", "globe thistle"]
# print("First three entries: ", flowers_list[:3])
# print("last three entries: ", flowers_list[-3:])
# flowers_list.remove('globe thistle')
# print(flowers_list)
# flowers_list.append('rose')
# flowers_list.append('lilly')
# print(flowers_list)


#How to append or remove multiple items in the list.
# hardcover_sales = [139, 128, 172, 139, 191, 168, 170]
# print("Length of the list:", len(hardcover_sales))
# print("Entry at index 2:", hardcover_sales[2])
# print("Minimum:", min(hardcover_sales))
# print("Maximum:", max(hardcover_sales))
# print("Total books sold in one week:", sum(hardcover_sales))
# print("Average books sold in first five days:", sum(hardcover_sales[:5])/5)
# print("Average books sold in last five days:", sum(hardcover_sales[-5:])/5)

# -------------------------------------------------------------------
# flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
# print(flowers.split(","))

# alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
# address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"
# letters = alphabet.split(".")
# formatted_address = address.split(",")
# print(letters)
# print(formatted_address)

# --------------------------------------------------------------------------------------------------------
# test_ratings = [1, 2, 3, 4, 5]
# test_liked = [i>=4 for i in test_ratings]
# print(test_liked)

# test_unliked = [i<4 for i in test_ratings]
# print(test_unliked)
# ------------------------------------------------------------------------------------------------------------
# Complete the function
# def percentage_liked(ratings):
#     list_liked = [i >= 4 for i in ratings]
#     percentage_liked = sum(list_liked)/len(list_liked)
#     return percentage_liked

#     alpha = sum(list_liked)/len(list_liked) # Alternatively
#     return alpha

# giga = percentage_liked([1, 2, 3, 4 ,5 ,4, 5, 1])
# print(giga)

# def agam(sora):
#     agam = sora + 3
#     return agam
# bagam = agam(2)
# print(bagam)
# ---------------------------------------------------------
# user_list01 = "920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078" # one sting element
# user_list02 = "920344", "1043553", "1204334", "1458996", "1503323", "1593432", "1623463", "1843064", "1930992", "2001078" 
# user_list = '920344', '1043553', '1204334', '1458996', '1503323', '1593432', '1623463', '1843064', '1930992', '2001078'
# num_users = list(user_list)
# print(num_users[:5])
# print(num_users[-3:])
# num_users03 = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
# print(num_users)
# print(num_users03)
# print(type(num_users))
# print(type(num_users03))
# print(type(num_users[0]))
# print(type(num_users03[0]))
# # ---------------------------------------------------------
# Say you're doing analytics for a website. You need to write a function that returns the percentage growth in the total number of users relative to a specified number of years ago.

# Your function percentage_growth() should take two arguments as input:

# num_users = Python list with the total number of users each year. So num_users[0] is the total number of users in the first year, num_users[1] is the total number of users in the second year, and so on. The final entry in the list gives the total number of users in the most recently completed year.
# yrs_ago = number of years to go back in time when calculating the growth percentage
# For instance, say num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078].

# if yrs_ago = 1, we want the function to return a value of about 0.036. This corresponds to a percentage growth of approximately 3.6%, calculated as (2001078 - 1930992)/1930992.
# if years_ago = 7, we would want to return approximately 0.66. This corresponds to a percentage growth of approximately 66%, calculated as (2001078 - 1204334)/1204334.
# Your coworker sent you a draft of a function, but it doesn't seem to be doing the correct calculation. Can you figure out what has gone wrong and make the needed changes?

# num_users = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# def percentage_growth(num_users, yrs_ago):
#     growth = (num_users[len(num_users) -1] - num_users[len(num_users) - yrs_ago - 1]) / num_users[len(num_users)-yrs_ago - 1]
#     return growth

# # Do not change: Variable for calculating some test examples
# num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# # Do not change: Should return .036
# print(percentage_growth(num_users_test, 1))

# # Do not change: Should return 0.66
# print(percentage_growth(num_users_test, 7))
# ----------------------------------------------------------
#-----------------------------------------------------------


###          ##################
 ###       ############
  ###     #########
    ###  ######
     #######

                                                                        
#1. 
# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# hands = [
#     ['J', 'Q', 'K'],
#     ['2', '2', '2'],
#     ['6', 'A', 'K'], # (Comma after the last element is optional) #hands = [['J', 'Q', 'K'], ['2', '2', '2'], ['6', 'A', 'K']]
# ]

# random_things = [46, 'flying mountains', 2.9, True, help]
# print(random_things)
# help(list)

#---------------------------------------------------
def tea_cup_printer():
    for i in range(9):
        for j in range(9):
            if i == 0 or j == 4:
                print("T", end=" ")
            elif i > 0 and j == 4 - i:
                print("T", end=" ")
            elif i > 0 and j == 4 + i:
                print("T", end=" ")
            else:
                print(" ", end=" ")
        print()

tea_cup_printer()
print(tea_cup_printer())
#------------------------------------------------------
#------------------------------------------------------

# def cube_printer():
#     for i in range(3):
#         for j in range(3):
#             print("*", end=" ")
#         print()
# cube_printer()

#-------------------------------------------------------
#-------------------------------------------------------

# def print_hollow_square():
#     for i in range(3):
#         for j in range(3):
#             if i == 0 or i == 3 - 1 or j == 0 or j == 3 - 1:
#                 print("#", end=" ")
#             else:
#                 print(" ", end=" ")
#         print()
# print_hollow_square()
# Example: Printing a hollow square with "side length of 5"
# print_hollow_square(5)
#--------------------------------------------------------------
###          ##################
 ###       ############
  ###     #########
    ###  ######
     #######



hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'], # (Comma after the last element is optional)
]

# print(hands[2])
# my_favourite_things = [32, 'raindrops on roses', help]
# print(my_favourite_things)

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# # print(planets[3:])
# # print(planets[0:4])
# # print(planets[2:-3])
# # print(planets[1:-1])
# # print(planets[:4])
# planets[3] = 'Malachandra'
# # print(planets[3])
# # print(planets)

# planets[:3] = ['Mur', 'Vee', 'Ur']
# # print(planets)
# # print(len(planets))

# print(planets[0:len(planets)])

# sorted(planets)
# print(planets)

# print(sorted, help)
# help(sorted)

# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# addition_of = [12, 45, 9, 0, 29, 33]

# # y = sorted(planets)
# p = sum(addition_of)
# q = max(addition_of)
# # print(y)
# print(q)

# x = 12
# # x is a real number, so its imaginary part is 0.
# print(x.imag)
# c = 12 + 3j
# print(c.imag)
# y = x.bit_length()
# z = c.bit_length()
# print(y)
# print(z)
# planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
# planets.remove('Mercury')
# planets.append('Pluto')
# print(planets[0:len(planets)], end='\n')
# print(planets.pop(1))
# print(planets.index('Pluto'))
# print("Earth" in planets)s
# print("Flight" in planets)
# t = (1, 2, 3)
# print(t)

# x = 11
# y = x.as_integer_ratio()
# print(y[0])


# def select_second(L):
#     if len(L) < 2:
#         return None
#     return L[1]
# print(select_second(['A', 2, True]))

x = [1, 2], [4], [98, -1], ['A', 'B', 'C', 'D']
print(type(x))
print(type(x[3]))
print(x[3])
print(type(x[2]))
print(x[2])








