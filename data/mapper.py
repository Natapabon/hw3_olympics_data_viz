import matplotlib.pyplot as plt

# draw a simple line chart showing population growth over the last 115 years
years = [1900, 1950, 1955, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
pops = [1.6, 2.5, 2.6, 3.0, 3.3, 3.6, 4.2, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9]

# plot our chart with data above
plt.plot(years,pops, color=(0/255, 100/255, 100/255), linewidth=3.0)

# Label for the Y side (left hand of the chart) 
plt.ylabel("World population by Billions")
# Label for the X side (bottom of the chart)
plt.xlabel("Population Growth by YEAR")

# add a title to the chart
plt.title("World population Growth", pad="20")

# run the show method (this lives inside the pyplot packages)
# this will generate a graph in a new window

plt.show()