import re
import pandas as pd

def process_csv(input_file, output_file):
    
    with open(f'./output_data/{input_file}', 'r') as file:
        data = file.read()
    data = re.sub(r'\s*,\s*', ',', data) # removes all spaces around commas
    
    with open('./output_data/temp.csv', 'w') as file:
        file.write(data)
    
    df = pd.read_csv('./output_data/temp.csv', header=None, on_bad_lines='skip')
    df = df[df.count(axis=1) >= 3] # removes rows with less than 3 columns
    df[2] = df[2].str.replace("'", "") # removes all single quotes for the progression column
    df.to_csv(f'./output_data/{output_file}', index=False, header=False)
    file.close()

