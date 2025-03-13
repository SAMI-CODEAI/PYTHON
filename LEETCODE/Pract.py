import matplotlib.pyplot as plt
import numpy as np

# Data steps during the sorting process
steps = [
    [3, 5, 9, 7, 1, 4, 6, 8, 2],  # Initial sequence
    [1, 2, 3, 5, 9, 7, 4, 6, 8],  # After pivot = 2
    [1, 2, 3, 5, 7, 4, 6, 8, 9],  # After pivot = 8
    [1, 2, 3, 4, 5, 6, 7, 8, 9],  # Fully sorted
]

# Stack the data for visualization
steps_stacked = np.array(steps)

# Visualize the data as a single bar graph
plt.figure(figsize=(10, 6))
for i in range(steps_stacked.shape[1]):
    plt.bar(i, steps_stacked[:, i], color=plt.cm.viridis(i / steps_stacked.shape[1]))

# Adding labels and title
plt.title("Quicksort Simulation: Progression of Sorting")
plt.xlabel("Array Index")
plt.ylabel("Value")
plt.show()
