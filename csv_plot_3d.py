import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

file_pass = 'C:/Users/pokeevil/Desktop/WorkSpace/UEC/fuzzy_sys/fuzzysystem_with_c++/Chikkuji/'
# file_name = 'data_test_new.csv'
file_name = 'data_test_new_range_error.csv'
data = pd.read_csv(file_pass + file_name)
print(data)

x1 = data['x1']
x2 = data['x2']
y = data['y']
tom = data['ToM']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# # as points
# ax.scatter(x1[tom == 0], x2[tom == 0], y[tom == 0], c='red', label='Tranning data', linewidth=0.3)
# ax.scatter(x1[tom == 1], x2[tom == 1], y[tom == 1], c='blue', label='Fuzzy model', linewidth=0.4)
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')
# ax.set_title('Fuzzy Modeling')
# ax.legend()
# plt.show()

# as wireframe
# get data of ToM==0
data_0 = data[data['ToM'] == 0]
x1_0 = data_0['x1'].values
x2_0 = data_0['x2'].values
y_0 = data_0['y'].values

# get data of ToM==1
data_1 = data[data['ToM'] == 1]
x1_1 = data_1['x1'].values
x2_1 = data_1['x2'].values
y_1 = data_1['y'].values

# plot data_0
X_0, Y_0 = np.meshgrid(np.unique(x1_0), np.unique(x2_0))
Z_0 = y_0.reshape(X_0.shape)
ax.plot_wireframe(X_0, Y_0, Z_0, color='blue', linewidth=0.3)

# plot data_1
X_1, Y_1 = np.meshgrid(np.unique(x1_1), np.unique(x2_1))
Z_1 = y_1.reshape(X_1.shape)
ax.plot_wireframe(X_1, Y_1, Z_1, color='red', linewidth=0.4)

ax.set_title('Modeling Result')
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')
ax.legend()

plt.tight_layout()
plt.show()
