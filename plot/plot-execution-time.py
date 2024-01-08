import matplotlib.pyplot as plt

fig, ax = plt.subplots()

states = ['Translating', 'Onboarding', 'Instantiation']
ax.set_xticklabels(states, rotation=30)
counts = [1, 6.32, 83.06]
bar_colors = ['grey']
ax.bar(states, counts, color=bar_colors)
ax.set_ylabel('Time(s)')
ax.set_title('Average execution time of the intent framework elements')

plt.plot()

plt.show()


