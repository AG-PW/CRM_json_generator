import pandas as pd
import json

input_file = 'input/data.csv'

df = pd.read_csv(input_file, sep=';')

output_dir = 'output/'
for index, row in df.iterrows():
    output_file = output_dir + str(index) + '.json'
    with open(output_file, 'w') as f:
        json.dump(row.to_dict(), f)

