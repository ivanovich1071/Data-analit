from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

import csv

import pandas as pd
import matplotlib.pyplot as plt
driver = webdriver.Chrome()
url = 'https://www.divan.ru/category/pramye-divany'
driver.get(url)
time.sleep(5)
prices = driver.find_elements(By.XPATH, "//span[@data-testid='price']")

# Сохранение цен в CSV файл
with open('sofa_prices.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Price'])
    for price in prices:
        price_text = price.text.replace('руб.', '').replace(' ', '').strip()
        writer.writerow([price_text])

driver.quit()

# Обработка данных с помощью Pandas
df = pd.read_csv('sofa_prices.csv')
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df = df.dropna()

# Вычисление средней цены
mean_price = df['Price'].mean()
print(f'Средняя цена: {mean_price:.2f} руб.')

# Построение гистограммы
plt.hist(df['Price'], bins=20, edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена, руб.')
plt.ylabel('Количество')
plt.show()
