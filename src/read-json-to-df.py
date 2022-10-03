# Step 1 - Read from files
import pandas as pd
from setuptools import PEP420PackageFinder

NUMBER_OF_PERSONS = 16
list_person = [f'p{"0" if i < 10 else ""}{i}' for i in range (1, (NUMBER_OF_PERSONS+1), 1)]
print(list_person)
  
list_relevant_files = ['calories.json', 'distance.json', 'exercise.json', 'heart_rate.json']


def getting_json_data (file_path):
  df = pd.read_json(file_path)
  return df


for person in list_person:
  for file in list_relevant_files:
    df = getting_json_data (f'raw_data/{person}/fitbit/{file}')
    print (f'{person} {file}', df.head())

