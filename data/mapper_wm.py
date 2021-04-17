import matplotlib.pyplot as plt


years = ["1924", "1928", "1932", "1936", "1948", "1952", "1956", "1960", "1964", "1968", "1972", "1976", "1980", "1984", "1988", "1992", "1994", "1998", "2002", "2006", "2010", "2014"]
women = [6, 6, 6, 9, 15, 18, 27, 39, 46, 46, 45, 51, 51, 54, 63, 99, 111, 189, 208, 232, 233, 272]
men = [112, 83, 110, 99, 125, 118, 123, 108, 139, 153,155, 159, 167, 168, 201, 226, 232, 258, 273, 299, 296, 340] 


fig, ax = plt.subplots()

line1 = ax.plot(years, men, label="men", color="navy")
line2 = ax.plot(years, women, label="women", color="darkturquoise")

ax.set_ylabel('Total medals won')
ax.set_xlabel('Winter Olympics years')

ax.legend()

plt.show()