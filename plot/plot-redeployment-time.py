import matplotlib.pyplot as plt

fig, ax = plt.subplots()

states = ['Slice deletion', 'Onboarding', 'Instantiation', 'Total re-deployment']
ax.set_xticklabels(states, rotation=25)

counts = [43.59, 6.16, 82.66, 132.41]

bar_colors = ['grey']

# Criando as barras
bars = ax.bar(states, counts, color=bar_colors)

# Adicionando os valores exatos nas barras
for bar, count in zip(bars, counts):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height, f'{count:.2f}', ha='center', va='bottom')

ax.set_ylabel('Time(s)')

plt.text(2.0, -40, 'Fig 3 - Average execution time of the intent framework elements on redeployment', ha='center', fontweight='bold')

plt.tight_layout()

plt.savefig('redeployment-time.pdf')
plt.show()
