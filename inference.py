import fuzzification as f

RULE_NUMBER = 54

def inference(input_dict):
    chest_pain = f.cp_fuzzification(int(input_dict['chest_pain']))
    cholesterol = f.c_fuzzification(int(input_dict['cholestrol']))
    ecg = f.ECG_fuzzification(float(input_dict['ecg']))
    exercise = f.exercise_fuzzification(int(input_dict['exercise']))
    thallium = f.thallium_fuzzification(int(input_dict['thallium_scan']))
    age = f.age_fuzzification(int(input_dict['age']))
    blood_pressure = f.bp_fuzzification(int(input_dict['blood_pressure']))
    blood_sugar = f.bs_fuzzification(int(input_dict['blood_sugar']))
    heart_rate = f.h_fuzzification(int(input_dict['heart_rate']))
    old_peak = f.old_fuzzification(float(input_dict['old_peak']))
    sex = f.sex_fuzzification(int(input_dict['sex']))


    def get_item(item, member):
        if item == 'chest_pain':
            return chest_pain[member]
        if item == 'cholesterol':
            return cholesterol[member]
        if item == 'ECG':
            return ecg[member]
        if item == 'exercise':
            return exercise[member]
        if item == 'thallium':
            return thallium[member]
        if item == 'age':
            return age[member]
        if item == 'blood_pressure':
            return blood_pressure[member]
        if item == 'blood_sugar':
            return blood_sugar[member]
        if item == 'maximum_heart_rate':
            return heart_rate[member]
        if item == 'old_peak':
            return old_peak[member]
        if item == 'sex':
            return sex[member]

    results = {
        'healthy': 0,
        'sick_1': 0,
        'sick_2': 0,
        'sick_3': 0,
        'sick_4': 0
    }
    i = 1
    file = open('rules.fcl', 'r')

    for rule in file:
        rule = (rule.replace('(', '')).replace(')', '')
        start = rule.index('IF') + 3
        end = rule.index('THEN')
        if_clause = rule[start: end - 1].split(' ')
        start = end + 5
        end = rule.index(';')
        then_clause = rule[start: end].split(' ')
        result = 0
        if len(if_clause) == 3:
            # print('1', if_clause[0], if_clause[2])
            result = get_item(if_clause[0], if_clause[2])
        else:  # len = 7
            # print('2', if_clause[3])
            # print('3', if_clause[0], if_clause[2])
            # print('4', if_clause[4], if_clause[6])
            operator = if_clause[3]
            x = get_item(if_clause[0], if_clause[2])
            y = get_item(if_clause[4], if_clause[6])
            if operator == 'AND':
                result = min(x, y)
            else:  # operator = 'OR'
                result = max(x, y)
        # print(i, then_clause)
        results[then_clause[2]] = max(results[then_clause[2]], result)
        i += 1
        if i == RULE_NUMBER:
            break

    file.close()
    # print(results)
    return results


# inference({'chest_pain': '2', 'cholestrol': '182', 'ecg': '0.8',
#            'exercise': '1', 'thallium_scan': '7', 'age': '31',
#            'blood_pressure': '154', 'blood_sugar': '104',
#            'heart_rate': '34', 'old_peak': '4.8', 'sex': '0'}
#           )
