import pandas as pd
import json

# Read the CSV file
df = pd.read_csv('movies_initial.csv')

# Save dataframe as Json
df.to_json('movies.json', orient='records')

# Read the Json file
with open('movies.json') as file:
    data = json.load(file)

for i in range(100):
    movie = data[i]
    print(movie)
    break