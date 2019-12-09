import pandas as pd
import urllib.request
import matplotlib.pyplot as plt

school = {'Name':['Jeff','Carrol','Kyle','Adrian','Jessica','Scott','Tanner','Kelly','Brittney','Joe'],
          'Age':[18,17,15,15,16,17,18,19,18,14],
          'Grade':[12,11,9,10,11,12,12,11,10,9]}

df = pd.DataFrame(school)
print(df)

df2 = df.sort_values('Grade')
print(df2)

df2 = df.sort_values('Age')
print(df2)

df2 = df.sort_values(['Grade','Age'])
print(df2)

df2 = df.sort_values(['Grade','Age','Name'])
print(df2)

df2 = df.sort_values(['Grade','Age','Name'], ascending = False)
print(df2)

df2 = df.sort_values(['Grade','Age','Name'], ascending = [False, True, True])
print(df2)

