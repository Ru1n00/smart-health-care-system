import csv
from random import choice as randchoice
import os

def get_psychiatric_disorder(patient_data):
    file = 'latest_psychiatric_disorder_dataset.csv'
    file = os.path.join(os.getcwd(), f'psychiatric_ai/{file}')

    age = patient_data['age']
    gender = patient_data['gender']
    education_level = patient_data['education_level']
    symptom_checklist = patient_data['symptom_checklist']
    behavior_patterns = patient_data['behavior_patterns']
    diagnostic_tests = patient_data['diagnostic_tests']
    lifestyle_factors = patient_data['lifestyle_factors']
    stressors = patient_data['stressors']


    psychiatric_disorder = ['OCD', 'PTSD', 'Substance Use Disorders', 'Bipolar Disorder', 'Schizophrenia',
    'Eating Disorders,' 'Other', 'ADHD', 'Depression', 'Anxiety',
    'Personality Disorders']

    with open(file, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        print(header)

        for row in reader:
            if education_level == row[2].lower() and symptom_checklist == row[6].lower() and behavior_patterns == row[7].lower() and diagnostic_tests == row[8].lower() and lifestyle_factors == row[9].lower() and stressors == row[10].lower():
                print('Matched:', row)
                return row[-1]
        else:
            print('random:', randchoice(psychiatric_disorder))
            return randchoice(psychiatric_disorder)
    