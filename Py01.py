#Lets spam a bit
# spam_amount = 0
# print(spam_amount)

# Ordering Spam, egg, Spam, Spam, bacon and Spam (4 more servings of Spam)
# spam_amount = spam_amount + 9
# print(spam_amount)
# if spam_amount > 0:
#     print("But I don't want ANY spam!")

# viking_song = "Spam " * spam_amount
# print(viking_song)
# ----------------------------------------------------------------------------------
# spam_amount = 0
# print(spam_amount)
# ----------------------------------------------------------
# x= abs(-0.59)
# y = round(-263.958123456789, 5)
# print(y)

# help(round(-2.01))                                                                           
# y = round('alpha')                                                                           
# print(y)
# --------------------------------
# --------------------------------
# print(1, 2, 3, sep='@')
# help(print)
#---------------------------------
# --------------------------------
# def most_difference(a, b, c):
#     diff1 = abs(a - b)
#     diff2 = abs(b - c)
#     diff3 = abs(a - c)
#     return max(diff1, diff2, diff3)

# m_diff = most_difference(159, 213, 67)
# print(m_diff)

# def can_run_for_president(age, is_natural_born_citizen):
#     """Can someone of the given age and citizenship status run for president in the US?"""
#     # The US Constitution says you must be a natural born citizen *and* at least 35 years old
    # return is_natural_born_citizen and (age >= 35)

# print(can_run_for_president(19, True))
# print(can_run_for_president(55, False))
# print(can_run_for_president(55, True))


# True or True and False
# g = True and False
# print(g)
# g1 = False and True
# print(g1)
# h = True and True
# print(h)
# h1 = False and False
# print(h1)

# -------------------
# g = True or False
# print(g)
# g1 = False or True
# print(g1)
# h = True or True
# print(h)
# h1 = False or False
# print(h1)

#----------------

# j = not True
# print(j)

# k = 3 | 2
# print(k)
# ----------------------------

# def inspect(x):
#     if x == 0:
#         print(x, "is zero")
#     elif x > 0:
#         print(x, "is positive")
#     elif x < 0:
#         print(x, "is negative")
#     else:
#         print(x, "is unlike anything I've ever seen...")

# inspect(0)
# inspect(-15)

# if 0:
#     print(0)
# elif "spam":
#     print("spam")

     #
    ###
  #######
   ####
  ######

# def to_smash(total_candies):
#     print("Splitting", total_candies, "candy" if total_candies == 1 else "candies") # Remember
#     return total_candies % 3
# to_smash(91)
# to_smash(1)    
# def concise_is_negative(number):
#     return number < 0
# print(concise_is_negative(-9))

# ---------------------------------------
# def wants_all_toppings(ketchup, mustard, onion):
#     """Return whether the customer wants "the works" (all 3 toppings)
#     """
#     return ketchup and mustard and onion
# print(wants_all_toppings(5, 5, 5))
# print(wants_all_toppings(-5, -5, -5))
# ---------------------------------------
# def wants_plain_hotdog(ketchup, mustard, onion):
#     """Return whether the customer wants a plain hot dog with no toppings.
#     """
#     return not ketchup and not mustard and not onion #Alternatively return not (ketchup and mustard and onion)
# print(wants_plain_hotdog(5, 5, 5))  
# print(wants_plain_hotdog(-5, -5, -5))
# print(wants_plain_hotdog(0, 0, 0))
# ---------------------------------------
# def exactly_one_sauce(ketchup, mustard, onion):
#     """Return whether the customer wants either ketchup or mustard, but not both.
#     (You may be familiar with this operation under the name "exclusive or")
#     """
#     return (ketchup and not mustard) or (mustard and not ketchup) # This i XOR - 0110
# print(exactly_one_sauce(0, 1, 1))
# print(exactly_one_sauce(2, 0, -1))
# print(exactly_one_sauce(0, 0, 12))
# print(exactly_one_sauce(1, 1, -4))
# ---------------------------------------
            #6666
          #66   
          #6666666
          #66   66
            #666
# ---------------------------------------
# print(bool(0))
# print(bool(5))
# print(int(True))
# print(int(False))
#-----------------------------------------
# Hint: You may have already found that int(True) is 1, and int(False) is 0.

# def exactly_one_topping(ketchup, mustard, onion):
#     """Return whether the customer wants exactly one of the three available toppings
#     on their hot dog.
#     """
#     #pass
#     #return (int(ketchup)+int(mustard)+int(onion))==1
#     return (ketchup + mustard + onion) == 1
# ----------------------------------------------------------------
# def should_hit(dealer_total, player_total, player_low_aces, player_high_aces):

#     return False

# print(should_hit(18, 20, 3, 7))
# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#  print(x)
#----------------------------------------------------------------------
# import datetime

# mydate = datetime.datetime.now()

# print("__str__() string: ", mydate.__str__())
# print("str() string: ", str(mydate))

# print("__repr__() string: ", mydate.__repr__())
# print("repr() string: ", repr(mydate))

#---------------------------------------------------------------------
# import datetime

# mydate1 = datetime.datetime.now()
# mydate2 = eval(repr(mydate1))

# print("mydate1 repr() string: ", repr(mydate1))
# print("mydate2 repr() string: ", repr(mydate2))

# print("the values of the objects are equal: ", mydate1==mydate2)
#---------------------------------------------------------------------



