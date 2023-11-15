# Import the sorting functions from algorithm_functions.py
from algorithm_functions \
import selection_sort, bubble_sort, merge_sort, quick_sort

import random


numberOfValues = int(input("Enter the number of random values to sort: "))
randomNumbers = [random.randint(1, 10000) for _ in range(numberOfValues)]
''' print("Original List:", randomNumbers) '''

algorithmType = int(input("\n1: Selection Sort"
                          "\n2: Bubble Sort"
                          "\n3: Merge Sort"
                          "\n4: Quick Sort"
                          "\nWhat algorithm would you choose to sort: "))



if algorithmType == 1:
    print("\nSelection Sort selected!")
    sortedNumbers, timeTaken = selection_sort(randomNumbers)  # Use selection_sort for Selection Sort
elif algorithmType == 2:
    print("\nBubble Sort selected!")
    sortedNumbers, timeTaken = bubble_sort(randomNumbers)  # Use bubble_sort for Bubble Sort
elif algorithmType == 3:
    print("\nMerge Sort selected!")
    sortedNumbers, timeTaken = merge_sort(randomNumbers)  # Use merge_sort for Merge Sort
elif algorithmType == 4:
    print("\nQuick Sort selected!")
    sortedNumbers, timeTaken = quick_sort(randomNumbers)  # Use quick_sort for Quick Sort
else:
    print("\nInvalid algorithm type. Please enter 1, 2, 3, or 4.")



if algorithmType in {1, 2, 3, 4}:
    # print("Sorted List:", sortedNumbers)
    print(f"Time taken to sort: {timeTaken:.6f} seconds")