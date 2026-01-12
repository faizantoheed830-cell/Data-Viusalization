import matplotlib.pyplot as plt

squares = [1,4,9,16,25,36]
fig , ax = plt.subplots()  # Fig Variable represents the collection of plots in a label & ax variable each plot

ax.plot(squares , linewidth = 3)

ax.set_title("Square Numbers" , fontsize = 24)
ax.set_xlabel("Value" , fontsize = 14)
ax.set_ylabel("Square of value" , fontsize = 14)

ax.tick_params(axis = 'both' , labelsize = 14)

plt.show()