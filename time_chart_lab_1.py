import matplotlib.pyplot as plt

# Data for Python execution times
elements = [1000, 2000, 3000, 4000, 5000, 6000]
bubble_sort_python = [0.0403, 0.1706, 0.3818, 0.6905, 1.0788, 1.5729]
insertion_sort_python = [0.0162, 0.0711, 0.1534, 0.2836, 0.4296, 0.6394]
quicksort_hoare_python = [0.001, 0.0021, 0.0032, 0.0044, 0.0056, 0.007]

# Data for C++ execution times
bubble_sort_cpp = [0.009, 0.034, 0.076, 0.136, 0.213, 0.314]
insertion_sort_cpp = [0.003, 0.012, 0.027, 0.052, 0.08, 0.111]
quicksort_hoare_cpp = [0, 0.001, 0, 0, 0.001, 0.001]

# Plotting the results for Python
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(elements, bubble_sort_python, label="BubbleSort", marker='o')
plt.plot(elements, insertion_sort_python, label="InsertionSort", marker='o')
plt.plot(elements, quicksort_hoare_python, label="QuickSort Hoare", marker='o')
plt.title('Python Execution Time')
plt.xlabel('Number of Elements')
plt.ylabel('Execution Time (seconds)')
plt.legend()

# Plotting the results for C++
plt.subplot(1, 2, 2)
plt.plot(elements, bubble_sort_cpp, label="BubbleSort", marker='o')
plt.plot(elements, insertion_sort_cpp, label="InsertionSort", marker='o')
plt.plot(elements, quicksort_hoare_cpp, label="QuickSort Hoare", marker='o')
plt.title('C++ Execution Time')
plt.xlabel('Number of Elements')
plt.ylabel('Execution Time (seconds)')
plt.legend()

plt.tight_layout()
plt.show()
