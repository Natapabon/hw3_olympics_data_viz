# number of men with total GOLD medals: 1310 / women: 611

import matplotlib.pyplot as plt

values = [1310, 611]
labels = ["Men", "Women"]
colors = ["yellow", "orange"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()