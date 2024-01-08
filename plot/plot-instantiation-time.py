import matplotlib.pyplot as plt

fig, ax = plt.subplots()

states = ['2', '3', '4', '5', '6']
counts = [83.06, 97.97, 113.61, 128.12, 144.63]

bar_colors = ['grey']

ax.bar(states, counts, color=bar_colors)

ax.set_ylabel('Instantiation Time(s)')
ax.set_xlabel('Number of Virtual Functions')

ax.set_title('Average instantiation time according to the number of virtual functions')

plt.plot()
plt.show()