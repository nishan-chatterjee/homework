import numpy as np

y = np.array([[138], [147], [222], [282]])
x = np.array([[5, 9, 3], [3, 4, 4], [5, 6, 1], [6, 8, 3]])
x_transpose = x.transpose()

# formula used
# w = (((x_transpose dot x) inverse) dot x_transpose) dot y
dot_product = np.dot(x_transpose, x)
pre_final = np.dot(np.linalg.inv(dot_product), x_transpose)
w = np.dot(pre_final, y)
# print rounded to 3 decimal places
print(np.round(w, 3))

prediction_set = np.array([[4, 3, 2], [8, 10, 2]])
predicted = np.dot(prediction_set, w)
print("\n\n", np.round(predicted, 3))
