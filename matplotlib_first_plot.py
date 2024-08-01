from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

# Median Dev salaries by Age
dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

plt.bar(dev_x, dev_y, label='Developer')

# Median Python dev salaries
#py_dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 8364]

plt.bar(dev_x, py_dev_y, label='Python')

plt.xlabel('Ages')

plt.ylabel('Median Salary')

plt.title('Median Salary by Age')

plt.legend()

plt.tight_layout()

#plt.savefig('plot.png')

plt.show()
