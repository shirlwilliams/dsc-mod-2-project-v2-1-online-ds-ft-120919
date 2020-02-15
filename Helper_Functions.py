import pandas as pd
import seaborn as sns
import matplotlib as plt
%matplotlib inline

def df_hist(data):
    for col in data:
        if data[col].dtype != 0:
            data.col.hist(color='pink')
            plt.title(col)
            plt.show()