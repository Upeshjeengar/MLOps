import pandas as pd
df=pd.read_csv('Salary_Data.csv')
df['YearsExperience']=2+df['YearsExperience'] #adding 2 years
df.to_csv('Salary_Data.csv',index=False)