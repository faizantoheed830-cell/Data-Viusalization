import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
x_values = [1,2,3,4,5]

y_values = [1,4,9,16,25]


fig , ax = plt.subplots()  # Fig Variable represents the collection of plots in a label & ax variable each plot

ax.plot(x_values , y_values , linewidth = 3)
ax.scatter(x_values,y_values, s=100)
ax.set_title("Square Numbers" , fontsize = 24)
ax.set_xlabel("Value" , fontsize = 14)
ax.set_ylabel("Square of value" , fontsize = 14)

ax.tick_params(axis = 'both' , labelsize = 14)

plt.show()