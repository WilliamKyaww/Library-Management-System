# Import the sorting functions from algorithm_functions.py
from algorithm_functions import selection_sort, bubble_sort, merge_sort, quick_sort

import random

import matplotlib.pyplot as plt
import numpy as np

maxNum = int(input("Enter the maximum number of values to sort: "))
numbers = [i * maxNum // 10 for i in range(11)]

for j in range(10):
    randomNumbers = [random.randint(1, 10000) for _ in range(numbers)]
    sortedNumbers, timeTaken = selection_sort(randomNumbers)
    timeTakenArray = [0] + [timeTaken]






xpoints = numbers
ypoints = timeTakenArray

plt.plot(xpoints, ypoints)
plt.show()

