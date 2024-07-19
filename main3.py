import numpy as np
import matplotlib.pyplot as plt
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов
#  Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)
# Создание гистограммы
plt.hist(data, bins=30, edgecolor='black')

#  Добавление заголовка и меток осей
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')

#  Отображение гистограммы
plt.show()
# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

# Построение диаграммы рассеяния
plt.scatter(data_x, data_y, c='blue', alpha=0.5)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

# Отображение диаграммы
plt.show()