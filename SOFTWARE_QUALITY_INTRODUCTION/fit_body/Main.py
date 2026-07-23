from Health import Health

print("Please, choose calculator:")
print("Ideal Weight Calculator(1) \nbody Type Calculator(2) \nCalorieCalculator(3)")

userSelection = input()

if userSelection == "1":

    print("*************Ideal Weight Calculator*************")

    print("Please, enter you gender(male or female):")
    gender = input()

    print("Please, enter you height (cm):")
    height = input()
    height = int(height)

    result = Health.calculate_ideal_weight(gender, height)
    print("Your ideal weight(kg):", result)


elif userSelection == "2":

    print("************Body Type Calculator**************")

    print("Please, enter you bust (cm):")
    bust = input()
    bust = int(bust)

    print("Please, enter you waist (cm):")
    waist = input()
    waist = int(waist)

    print("Please, enter you hip (cm):")
    hip = input()
    hip = int(hip)

    result = Health.calculate_body_type(bust, waist, hip);
    print("Your body type:", result)


elif userSelection == "3":

    print("*************Calorie Calculator************")

    print("Please, enter you gender (male or female):")
    gender = input()

    print("Please, enter you age:")
    age = input()
    age = int(age)

    print("Please, enter you height (cm):")
    height = input()
    height = int(height)

    print("Please, enter you weight (kg):")
    weight = input()
    weight = int(weight)

    print("Please, enter your activity level (1-6):")
    for key in Health.activity:
        print(key)
    activity = input()
    activity = int(activity)
    activity = activity -1
    activity = list(Health.activity.values())[activity]

    result = Health.CalculatorCalorie(gender, age, height, weight, activity)
    print("Your daily recommended calorie intake:", result)


else:
    print("Invalid value.")
    