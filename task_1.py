import numpy as np
import matplotlib.pyplot as plt

hours = np.array([1, 2, 3, 5, 6, 8])
a_mark = np.array([10, 19, 28, 38, 51, 60])

weights = np.arange(1, 21)
mse_list = []

for w in weights:
    pred = w * hours
    mse = np.mean((pred - a_mark)**2)
    mse_list.append(mse)

lowest_index = mse_list.index(min(mse_list))
best_weight = weights[lowest_index]

print(f"The weight that gives the lowest MSE is: {best_weight}")

plt.figure(figsize=(8, 5))
plt.plot(weights, mse_list, marker='o', linestyle='-')
plt.xlabel("Weight")
plt.ylabel("Mean Squared Error (MSE)")
plt.title("Weight vs MSE")
plt.grid(True)

plt.show()