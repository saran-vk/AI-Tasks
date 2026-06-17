import numpy as np

hours = np.array([1, 2, 3, 5, 6, 8])
a_mark = np.array([10, 19, 28, 38, 51, 60])
new_stud = [4, 7, 9]

weights = np.arange(1, 21)
biases = np.arange(-10, 11)

min_mse = None
best_w = None
best_b = None

for w in weights:
    for b in biases:
        pred = w * hours + b
        mse = np.mean((pred - a_mark)**2)
        if min_mse is None or mse < min_mse:
            min_mse = mse
            best_w = w
            best_b = b

print(f"Best Weight: {best_w}, Best Bias: {best_b} (MSE: {min_mse:.2f})")

for x in new_stud:
    y = best_w * x + best_b
    print(f"Student studied {x} hrs -> predicted marks: {y}")