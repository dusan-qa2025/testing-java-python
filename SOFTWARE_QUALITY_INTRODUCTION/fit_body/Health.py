class Health:
    activity = {"Basal Metabolic Rate (BMR) (1)": 1,
                "Sedentary - little or no exercise (2)": 1.2,
                "Lightly Arctive - exercise/sports 1-3 times/week (3)": 1.375,
                "Moderately Arctive - exercise/sports 3-5 times/week (4)": 1.55,
                "Very Active - hard exercise/sports 6-7 times/week (5)": 1.725,
                "Extra Active - very hard exercise/sports or physical job (6)": 1.9}
    
    @staticmethod
    def calculate_ideal_weight(gender, height_cm):
        ideal_weight = -1
        correction = height_cm - 152

        if gender == "male" :
            ideal_weight = 48

            if correction > 0:
                ideal_weight += (correction * 1.1)

        elif gender == "female" :
            ideal_weight = 45.5

            if correction > 0:
                ideal_weight += (correction * 0.9)

        return ideal_weight

    @staticmethod
    def calculate_body_type(bust_Cm, waist_Cm, hip_Cm):
        shape = ""

        bust_Waist_Ratio = bust_Cm / waist_Cm
        hip_Waist_Ratio = hip_Cm / waist_Cm

        if (bust_Waist_Ratio < 1.4 and hip_Waist_Ratio < 1.4):
            shape = "Banana"
        elif (bust_Waist_Ratio - hip_Waist_Ratio >= 0.2):
            shape = "Apple"
        elif (hip_Waist_Ratio - bust_Waist_Ratio >= 0.2):
            shape = "Pear"   
        else:
            shape = "Hourglass"

        return shape

    @staticmethod
    def Calculator_Calorie(gender, age, height_Cm, weight_Kg, activity):
        calorie_Result = -1
        correction = 0

        if (gender == "male"):
            correction = 5
        elif (gender == "female"):
            correction = -161

        calorie_Result = (10 * weight_Kg + 6.25 * height_Cm - 5 * age + correction) * activity

        return calorie_Result
                         