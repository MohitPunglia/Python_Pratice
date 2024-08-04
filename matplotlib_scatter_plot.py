import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
# y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]

data = pd.read_csv('Matplotlib\ScatterPlots\data.csv')
view_count = data["view_count"]
likes = data["likes"]
ratio = data["ratio"]

plt.scatter(
    view_count,
    likes,
    c=ratio,
    cmap="summer",
    edgecolors="green",
    linewidths=1,
    alpha=0.75,
)

cbar = plt.colorbar()
cbar.set_label("Likes/Dislike Ratio")

plt.xscale("log")
plt.yscale("log")

plt.title("Trending Youtube Videos")
plt.xlabel("View Count")
plt.ylabel("Total Likes")

# plt.scatter(x, y)

plt.show()
