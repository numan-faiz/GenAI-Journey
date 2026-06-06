# matplotlib figure anatomy and visualization workflow--->use to make graphs
# because a picture is woth a thousand words so grapgh is better use matplotlib libraray
# it provides a figure that acts like a canvas on which various graphs and plots can be created

# axes: the individual; plot area that contains the x-axis and y axis
# 3d plotting---> represents data using three axis,y-axis,z-axis

# workflows--->statefull(pyplot syle) functtions operate on the current figure and axes
# object oreint (oo style) uses explicit figure and axes objects for greater control


# use oo style for clarity grapgh
# label pro[perly x-axis and y axis
# use descriptive labels for plots
import matplotlib.pyplot as plt
# object oriented workflows
fig, ax=plt.subplots()

# lables axes
ax.set_title("Blank figure example")
ax.set_xlabel("X-axis Label")
ax.set_ylabel("Y-axis Label")


# save to png
fig.savefig("blank_plot.png",dpi=100)
plt.show()


