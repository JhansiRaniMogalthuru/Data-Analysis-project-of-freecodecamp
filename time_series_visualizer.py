import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def draw_line_plot():
    df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)
    df = df[(df['value'] >= df['value'].quantile(0.025)) &
            (df['value'] <= df['value'].quantile(0.975))]

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.plot(df.index, df['value'], 'r', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')
    fig.savefig('line_plot.png')
    return fig

