import pandas as pd
from matplotlib import pyplot as plt

file_pass = 'C:/Users/pokeevil/Desktop/WorkSpace/UEC/fuzzy_sys/fuzzysystem_with_c++/Chikkuji/'
file_name = 'data_test.csv'
data = pd.read_csv(file_pass + file_name)

data0 = data.ToM==0
data1 = data.ToM==1

plt.plot(data[data0].x1, data[data0].y, "r")
plt.plot(data[data1].x1, data[data1].y, "b")
plt.show()
