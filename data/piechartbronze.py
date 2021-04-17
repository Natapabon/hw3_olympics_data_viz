# number of men with total BRONZE medals: 1315 / women: 604

import matplotlib.pyplot as plt

values = [1315, 604]
labels = ["Men", "Women"]
colors = ["brown", "red"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)


plt.show()