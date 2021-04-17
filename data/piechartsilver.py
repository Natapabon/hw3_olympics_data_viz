# number of men with total SILVER medals: 1319 / women: 611

import matplotlib.pyplot as plt

values = [1315, 611]
labels = ["Men", "Women"]
colors = ["lightblue", "grey"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)

plt.show()