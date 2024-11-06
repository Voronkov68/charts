import matplotlib.pyplot as plt 

plt.style.use('dark_background')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)
ax.set_title("Square Numbers", fontsize=14)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis="both", which="major", labelsize=14)
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]
ax.scatter(x_values, y_values, s=100 )
plt.show()