import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def draw_cat_plot():
    df = pd.read_csv('medical_examination.csv')

    df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

    df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
    df['gluc'] = (df['gluc'] > 1).astype(int)

    df_cat = pd.melt(df,
                     id_vars=['cardio'],
                     value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    fig = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio')
    fig.set_axis_labels("variable", "total")

    fig.savefig('catplot.png')
    return fig.fig

