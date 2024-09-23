import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Данные для таблицы
data = {
    'N': [1000, 2000, 3000, 4000, 5000, 6000],
    'B (BubbleSort)': [0.009, 0.034, 0.076, 0.136, 0.213, 0.314],
    'I (InsertionSort)': [0.003, 0.012, 0.027, 0.052, 0.08, 0.111],
    'H (QuickSort Hoare)': [0, 0.001, 0, 0, 0.001, 0.001]
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Добавляем столбцы N^2 и N*log(N)
df['N^2'] = df['N'] ** 2
df['N*log(N)'] = df['N'] * np.log(df['N'])

# Построение графиков
plt.figure(figsize=(12, 6))

# График для BubbleSort и InsertionSort против N^2
plt.subplot(1, 2, 1)
plt.plot(df['N^2'], df['B (BubbleSort)'], label='BubbleSort', marker='o')
plt.plot(df['N^2'], df['I (InsertionSort)'], label='InsertionSort', marker='o')
plt.title('BubbleSort and InsertionSort vs N^2')
plt.xlabel('N^2')
plt.ylabel('Execution Time (seconds)')
plt.legend()

# График для QuickSort Hoare против N*log(N)
plt.subplot(1, 2, 2)
plt.plot(df['N*log(N)'], df['H (QuickSort Hoare)'], label='QuickSort Hoare', marker='o')
plt.title('QuickSort Hoare vs N*log(N)')
plt.xlabel('N*log(N)')
plt.ylabel('Execution Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()
