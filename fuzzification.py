def point_result(x, point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    m = (y2 - y1) / (x2 - x1)
    # y − y1 = m(x − x1)
    y = y1 + m * (x - x1)

    return round(y, 2)

# Chest Pain
# region
def cp_fuzzification(x):
    cp = {
        'typical_anginal': 1 if x == 1 else 0,
        'atypical_anginal': 1 if x == 2 else 0,
        'non_anginal_pain': 1 if x == 3 else 0,
        'asymptomatic': 1 if x == 4 else 0
    }
    return cp


# endregion

# Blood Pressure
# region
def bp_low(x):
    if x <= 111:
        return 1
    elif 111 < x < 134:
        return point_result(x, (111, 1), (134, 0))
    else:
        return 0


def bp_medium(x):
    if x <= 127 or x >= 153:
        return 0
    elif 127 < x <= 139:
        return point_result(x, (127, 0), (139, 1))
    else:
        return point_result(x, (153, 0), (139, 1))


def bp_high(x):
    if x <= 142 or x >= 172:
        return 0
    elif 142 < x <= 157:
        return point_result(x, (142, 0), (157, 1))
    else:
        return point_result(x, (172, 0), (157, 1))


def bp_veryhigh(x):
    if x <= 154:
        return 0
    elif 154 < x <= 171:
        return point_result(x, (154, 0), (171, 1))
    else:
        return 1


def bp_fuzzification(x):
    bloodPressure = {
        'low': bp_low(x),
        'medium': bp_medium(x),
        'high': bp_high(x),
        'very_high': bp_veryhigh(x)
    }
    return bloodPressure


# endregion

# Cholesterol
# region
def c_low(x):
    if x <= 151:
        return 1
    elif 151 < x < 197:
        return point_result(x, (151, 1), (197, 0))
    else:
        return 0


def c_medium(x):
    if x <= 188 or x >= 250:
        return 0
    elif 188 < x <= 215:
        return point_result(x, (188, 0), (215, 1))
    else:
        return point_result(x, (250, 0), (215, 1))


def c_high(x):
    if 217 >= x >= 307:
        return 0
    elif 217 < x <= 263:
        return point_result(x, (217, 0), (263, 1))
    else:
        return point_result(x, (307, 0), (263, 1))


def c_veryhigh(x):
    if x <= 281:
        return 0
    elif 281 < x <= 347:
        return point_result(x, (281, 0), (347, 1))
    else:
        return 1


def c_fuzzification(x):
    cholesterol = {
        'low': c_low(x),
        'medium': c_medium(x),
        'high': c_high(x),
        'very_high': c_veryhigh(x)
    }
    return cholesterol


# endregion

# Blood Sugar
# region
def bs_fuzzification(x):
    if x < 120:
        return {'true': 0,
                'false': 1}
    else:
        return {'true': 1,
                'false': 0}


# endregion

# ECG
# region
def ECG_normal(x):
    if x <= 0:
        return 1
    elif 0 < x < 0.4:
        return point_result(x, (0, 1), (0.4, 0))
    else:
        return 0


def ECG_abnormal(x):
    if x <= 0.2 or x >= 1.8:
        return 0
    elif 0.2 < x <= 1:
        return point_result(x, (0.2, 0), (1, 1))
    else:
        return point_result(x, (1.8, 0), (1, 1))


def ECG_hypertrophy(x):
    if x <= 1.4:
        return 0
    elif 1.4 < x <= 1.9:
        return point_result(x, (1.4, 0), (1.9, 1))
    else:
        return 1


def ECG_fuzzification(x):
    heart_rate = {
        'normal': ECG_normal(x),
        'abnormal': ECG_abnormal(x),
        'hypertrophy': ECG_hypertrophy(x)
    }
    return heart_rate


# endregion

# Maximum Heart Rate
# region
def h_low(x):
    if x <= 100:
        return 1
    elif 100 < x < 141:
        return point_result(x, (100, 1), (141, 0))
    else:
        return 0


def h_medium(x):
    if x <= 111 or x >= 194:
        return 0
    elif 111 < x <= 152:
        return point_result(x, (111, 0), (152, 1))
    else:
        return point_result(x, (194, 0), (152, 1))


def h_high(x):
    if x <= 152:
        return 0
    elif 152 < x <= 210:
        return point_result(x, (152, 0), (210, 1))
    else:
        return 1


def h_fuzzification(x):
    heart_rate = {
        'low': h_low(x),
        'medium': h_medium(x),
        'high': h_high(x)
    }
    return heart_rate


# endregion

# Exercise
# region
def exercise_fuzzification(x):
    exercise = {
        'false': 1 if x == 0 else 0,
        'true': 1 if x == 1 else 0
    }
    return  exercise
# endregion

# OLD PEAK
# region
def old_low(x):
    if x <= 1:
        return 1
    elif 1 < x < 2:
        return point_result(x, (1, 1), (2, 0))
    else:
        return 0


def old_risk(x):
    if x <= 1.5 or x >= 4.2:
        return 0
    elif 1.5 < x <= 2.8:
        return point_result(x, (1.5, 0), (2.8, 1))
    else:
        return point_result(x, (4.2, 0), (2.8, 1))


def old_terrible(x):
    if x <= 2.5:
        return 0
    elif 2.5 < x <= 4:
        return point_result(x, (2.5, 0), (4, 1))
    else:
        return 1


def old_fuzzification(x):
    old_peak = {
        'low': old_low(x),
        'risk': old_risk(x),
        'terrible': old_terrible(x)
    }
    return old_peak


# endregion

# Thallium
# region
def thallium_fuzzification(x):
    thallium = {
        'normal': 1 if x == 3 else 0,
        'medium': 1 if x == 6 else 0,
        'high': 1 if x == 7 else 0
    }
    return thallium
# endregion

# Sex
# region
def sex_fuzzification(x):
    sex = {
        'male': 1 if x == 0 else 0,
        'female': 1 if x == 1 else 0
    }
    return sex
# endregion

# AGE
# region
def age_young(x):
    if x <= 29:
        return 1
    elif 29 < x < 38:
        return point_result(x, (29, 1), (38, 0))
    else:
        return 0


def age_mild(x):
    if x <= 33 or x >= 45:
        return 0
    elif 33 < x <= 38:
        return point_result(x, (33, 0), (38, 1))
    else:
        return point_result(x, (45, 0), (38, 1))


def age_old(x):
    if x <= 40 or x >= 58:
        return 0
    elif 40 < x <= 48:
        return point_result(x, (40, 0), (48, 1))
    else:
        return point_result(x, (58, 0), (48, 1))


def age_veryold(x):
    if x <= 52:
        return 0
    elif 40 < x <= 48:
        return point_result(x, (52, 0), (60, 1))
    else:
        return 1


def age_fuzzification(x):
    age = {
        'young': age_young(x),
        'mild': age_mild(x),
        'old': age_old(x),
        'very_old': age_veryold(x)
    }
    return age


# endregion

# OUTPUT
# region
def o_healthy(x):
    if x <= 0.25:
        return 1
    elif 0.25 < x < 1:
        return point_result(x, (0.25, 1), (1, 0))
    else:
        return 0


def o_sick1(x):
    if x <= 0 or x >= 2:
        return 0
    elif 0 < x <= 1:
        return point_result(x, (0, 0), (1, 1))
    else:
        return point_result(x, (2, 0), (1, 1))


def o_sick2(x):
    if x <= 1 or x >= 3:
        return 0
    elif 1 < x <= 2:
        return point_result(x, (1, 0), (2, 1))
    else:
        return point_result(x, (3, 0), (2, 1))


def o_sick3(x):
    if x <= 2 or x >= 4:
        return 0
    elif 2 < x <= 3:
        return point_result(x, (2, 0), (3, 1))
    else:
        return point_result(x, (4, 0), (3, 1))


def o_sick4(x):
    if x <= 3:
        return 0
    elif 3 < x <= 3.75:
        return point_result(x, (3, 0), (3.75, 1))
    else:
        1


def o_fuzzification(x):
    output = {
        'healthy': o_healthy(x),
        'sick_1': o_sick1(x),
        'sick_2': o_sick2(x),
        'sick_3': o_sick3(x),
        'sick_4': o_sick4(x)
    }
    return output
# endregion
