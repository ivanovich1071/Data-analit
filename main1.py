import pandas as pd
df = pd.read_csv('dz.csv')
print(df.columns.tolist())
average_salary_by_city = df.groupby('City')['Salary'].mean()


print("\nСредняя зарплата по городам:")
print(average_salary_by_city)
