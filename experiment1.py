import matplotlib.pyplot as plt

def author():
    return 'pwang387'

# pass the value of each portfolio
def plot_chart(df_learn, df_man, df_base, title):
    plt.plot(df_learn, label = 'Strategy Learner',color = 'blue' )
    plt.plot(df_man, label="Manual Strategy", color='red')
    plt.plot(df_base, label="Baseline", color='purple')
    plt.title(title)
    plt.xticks(rotation=45)
    plt.ylabel("Normalized Return")
    plt.legend()
    plt.savefig(title+" experiment1", bbox_inches="tight")
    #plt.show()
    plt.close()
