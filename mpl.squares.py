import matplotlib.pyplot as plt 
import seaborn as sns


squares = [1, 4, 9, 16, 25]
input_falues = list(range(1, 6))

plt.style.use('dark_background')
fig, ax = plt.subplots()

ax.plot(input_falues, squares, linewidth=3)
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square Of Value", fontsize=14)
ax.tick_params(axis='both', labelsize=14, labelcolor='red', rotation=45)


plt.show()

print(plt.style.available)