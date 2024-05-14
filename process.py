import re
import pandas as pd
import csv
def process_csv(input_file_path, output_file_path):
    
    with open(input_file_path, 'r') as file:
        data = file.read()
    data = re.sub(r'\s*,\s*', ',', data) # removes all spaces around commas
    
    with open('./output_data/temp.csv', 'w') as file:
        file.write(data)
    
    df = pd.read_csv('./output_data/temp.csv', header=None, on_bad_lines='skip')
    df = df[df.count(axis=1) >= 3] # removes rows with less than 3 columns
    df = df.map(lambda x: re.sub(r'\s{2,}', ' ', str(x))) # remove consecutive spaces
    df = df.map(lambda x: re.sub(r'(?<=\w)(?!\.)\s([A-Z])', r'. \1', str(x))) # adds a period after a word that also has a capital letter word after it
    df.to_csv(output_file_path, index=False, header=False, quoting=csv.QUOTE_NONNUMERIC) # adds qutoes around every column
    file.close()

#process_csv('./output_data/surprise/surprise_data.csv', 'test.csv')
