import pandas as pd

df = pd.read_csv('Crime_EX.csv')

df['Violent_crime_rate'].to_csv('newcsv2.csv')

df.set_index('Year', inplace = True)

df['Violent_crime_rate'].to_csv('newcsv2.csv')

df = pd.read_csv('newcsv2.csv')
print(df.head())

df = pd.read_csv('newcsv2.csv', index_col=0)
print(df.head())

df = pd.read_csv('newcsv2.csv', names = ['Date','Violent_crime_rate'], index_col=0)
print(df.head())


df.to_csv('newcsv3.csv')

df.to_csv('newcsv4.csv', header=False)
