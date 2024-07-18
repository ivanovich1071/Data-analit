import pandas as pd

#  DataFrame с данными из таблицы
data = {
    'ученик': ['Иван', 'Татьяна', 'Сергей', 'Нина', 'Павел', 'Анна', 'Егор', 'Галина', 'Ольга', 'Степан'],
    'математика': [8, 9, 6, 10, 10, 5, 6, 5, 4, 7],
    'физика': [8, 10, 7, 9, 10, 6, 7, 6, 5, 7],
    'химия': [7, 8, 7, 8, 8, 6, 6, 6, 5, 6],
    'английский язык': [6, 9, 6, 8, 8, 8, 7, 8, 9, 6],
    'русский язык': [7, 9, 7, 8, 8, 8, 6, 8, 9, 7]
}

df = pd.DataFrame(data)


print("Первые несколько строк DataFrame:")
print(df.head())

#  средняя  по каждому предмету
mean_scores = df.mean(numeric_only=True)
print("\nСредняя оценка по каждому предмету:")
print(mean_scores)

#  медианная оценку по каждому предмету
median_scores = df.median(numeric_only=True)
print("\nМедианная оценка по каждому предмету:")
print(median_scores)

#  Q1 и Q3 для оценок по математике
Q1_math = df['математика'].quantile(0.25)
Q3_math = df['математика'].quantile(0.75)
print("\nQ1 и Q3 для оценок по математике:")
print(f"Q1_math = {Q1_math}")
print(f"Q3_math = {Q3_math}")

#  IQR  по математике
IQR_math = Q3_math - Q1_math
print("\nIQR для оценок по математике:")
print(f"IQR_math = {IQR_math}")

#  стандартное отклонение по каждому предмету
std_deviation = df.std(numeric_only=True)
print("\nСтандартное отклонение по каждому предмету:")
print(std_deviation)

# +столбец «средний бал» для каждого ученика
df['средний бал'] = df.mean(axis=1, numeric_only=True)
print("\nDataFrame с добавленным столбцом «средний бал»:")
print(df)

#  медиана  по «среднему балу»
median_avg_score = df['средний бал'].median()
print("\nМедианная оценка по «среднему балу»:")
print(median_avg_score)

#  Q1 и Q3 по «среднему балу»
Q1_avg_score = df['средний бал'].quantile(0.25)
Q3_avg_score = df['средний бал'].quantile(0.75)
print("\nQ1 и Q3 по «среднему балу»:")
print(f"Q1_avg_score ={Q1_avg_score}")
print(f"Q3_avg_score = {Q3_avg_score}")

#  IQR по «среднему балу»
IQR_avg_score = Q3_avg_score - Q1_avg_score
print("\nIQR по «среднему балу»:")
print(f"IQR_avg_score = {IQR_avg_score}")
