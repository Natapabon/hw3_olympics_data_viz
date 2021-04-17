import matplotlib.pyplot as plt

country = ["USA", "CAN", "NOR", "URS", "FIN"]
medals = [653, 625, 457, 440, 434]
# golden = [167, 315, 159, 250, 66]
# silver = [319, 203, 171, 97, 147]
# bronze = [167, 107, 127, 93, 221]


# plot our chart with data above
plt.bar(country, medals, color=(30/110, 50/146, 100/183), linewidth=3.0)

# Label for the Y side (left hand of the chart) 
plt.ylabel("Total medlas won")

plt.show()