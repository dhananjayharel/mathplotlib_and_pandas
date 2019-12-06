import pandas as pd

df = pd.read_csv('Crime_EX.csv')

df['Violent_crime_rate'].to_csv('newcsv2.csv')

df.set_index('Year', inplace = True)

print(df.head())

df['Violent_crime_rate'].to_csv('newcsv2.csv')
