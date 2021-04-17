# number of men with medals: 386 / women: 239

import matplotlib.pyplot as plt

values = [386, 239]
labels = ["Men", "Women"]
colors = ["lightskyblue", "gold"]
explode = (0, 0.1)

plt.pie(values, labels=labels, colors=colors, explode=explode)
plt.show()