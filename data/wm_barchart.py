# number of men with total BRONZE medals: 1315 / women: 604


import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ["USA", "CAN", "NOR", "URS", "FIN"]
men_won = [410, 386, 359, 331, 328]
women_won = [243, 239, 98, 109, 106]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, men_won, width, label='Men')
rects2 = ax.bar(x + width/2, women_won, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Total medals won')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=-30, color="white")
ax.bar_label(rects2, padding=-30, color="white")

fig.tight_layout()

plt.show()



