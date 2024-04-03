# Condition_nal Statements
# print(5<3)
# print(7>2)

# var_1 = 1
# var_2 = 4
# print(var_1 < 4)
# print(var_2 >= 5)
# print(var_2 >= var_1)
# --------------------------

# def evaluate_temp(temp):
#     message = "Normal temperature."
#     if temp > 38:
#         message = "Fever!"
#     return message
# # body_temp = evaluate_temp(36)
# # print(body_temp)
# print(evaluate_temp(40))
#----------------------------------------
# "if...else" statements

# def evaluate_temp(temp):
#     if temp > 38:
#         message = "Fever!"
#     else:
#          message = "Fine!"
#     return message
# print(evaluate_temp(20))
# -----------------------------------------------
# def evaluate_marks(score):
#     if score > 70:
#         result = 'Distinction!'
#     elif score > 40:
#         result = 'Average'
#     else:
#         result = 'gone'
#     return result
# print(evaluate_marks(88))

# ----------------------------------------------------
# def get_taxes(earnings):
#     if earnings < 12000:
#         tax_owed = .25*earnings
#     else:
#         tax_owed = 0.30*earnings
#     return tax_owed

# ana_taxes = get_taxes(15000)
# bob_taxes = get_taxes(8500)
# print(ana_taxes)
# print(bob_taxes)
# ----------------------------------------
# def add_three_or_eight(ex):
#     if ex < 24:
#         alpha = ex + 3
#     elif ex >= 24:
#         alpha = ex + 8
#     return alpha
# print(add_three_or_eight(23))
# -------------------------------------------------
# def add_three_or_eight(number):
#     if number < 10:
#         result = number + 3
#     else:
#         result = number + 8
#     return result
# print(add_three_or_eight(11))
# -------------------------------------------------
# def get_dose(weight):
#     # Dosage is 1.25 ml for anyone under 5.2 kg
#     if weight < 5.2:
#         dose = 1.25
#     elif weight < 7.9:
#         dose = 2.5
#     elif weight < 10.4:
#         dose = 3.75
#     elif weight < 15.9:
#         dose = 5
#     elif weight < 21.2:
#         dose = 7.5
#     # Dosage is 10 ml for anyone 21.2 kg or over
#     else:
#         dose = 10
#     return dose
# print(get_dose(7))
# -----------------------------------
# def get_cookie(age_group):
#     if age_group < 5:
#         num_cookie = 1
#     elif age_group < 7:
#         num_cookie = 2
#     elif age_group < 9:
#         num_cookie = 3
#     else:
#         num_cookie = 4
#     return num_cookie
# print(get_cookie(7))
# Cookies_you_get = get_cookie(15)
# print("Here are your cookies, kid: ", Cookies_you_get)
# ----------------------------------------------------------

# def get_grade(score):
#     if score >= 90:
#         grade = 'A'
#     elif score >= 80:
#         grade = 'B'
#     elif score >= 70:
#         grade = 'C'
#     elif score >= 60:
#         grade = 'D'
#     else:
#         grade = 'F'
#     return grade
# stud_grade = get_grade(65)
# print("Your grade is: ", stud_grade)
# ----------------------------------------------------
# def get_water_bill(num_gallons):
#     if num_gallons <=8000:
#         bill = num_gallons*5/1000
#     elif num_gallons <=22000:
#         bill = num_gallons*6/1000
#     elif num_gallons <=30000:
#         bill = num_gallons*7/1000
#     else:
#         bill = num_gallons*10/1000
#     return bill
# print("Your bill is: ", get_water_bill(12000))
# -------------------------------------------------------------

def get_labels(food_type, serving_size, calories_per_serving, saturated_fat_g, trans_fat_g, sodium_mg, sugars_g):
    # Print messages based on findings
    if excess_sugar(sugars_g, calories_per_serving) == True:
        print("EXCESO AZÚCARES / EXCESS SUGAR")
    if excess_saturated_fat(saturated_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS SATURADAS / EXCESS SATURATED FAT")
    if excess_trans_fat(trans_fat_g, calories_per_serving) == True:
        print("EXCESO GRASAS TRANS / EXCESS TRANS FAT")
    if excess_sodium(calories_per_serving, sodium_mg) == True:
        print("EXCESO SODIO / EXCESS SODIUM")
    if excess_calories(food_type, calories_per_serving, serving_size) == True:
        print("EXCESO CALORÍAS / EXCESS CALORIES")

get_labels("solid", 32, 110, 2.5, 0, 400, 1)













