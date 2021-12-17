import matplotlib.pyplot as plt
from matplotlib import colors as mcolors

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



def plot_hists(df):
    df_grouped = df.groupby(['publish_year', 'occupation'], as_index=False).sum()
    df_grouped_top = df_grouped.sort_values(['publish_year','o'], ascending=False).groupby(['publish_year'], as_index=False).head(6)

    group_colors = {}
    colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
    colors = list(colors.values())

    unique_top_occupation_groups = [elem[0] for elem in df_grouped_top.groupby("occupation").sum().reset_index().values]
    for i, group_number in enumerate(unique_top_occupation_groups):
        group_colors[group_number] = colors[i + 15]

    years = np.unique(df_grouped_top.publish_year)

    fig, axs = plt.subplots(5, 2, figsize=(20, 30))
    for i, year in enumerate(years):
        year_df = df_grouped_top[df_grouped_top.publish_year == year]
        year_occupations = year_df.occupation.values
        
        for group_n, group_ in enumerate(year_occupations):
            temp_group = year_df[year_df.occupation == group_]
            axs[i // 2][i % 2].bar(
                group_,
                100 * temp_group.o.values[0] / year_df.o.sum(), 
                color=group_colors[group_],
                width=0.4,
                align='center'
            )
        axs[i // 2][i % 2].set_title(year, fontsize=20)
        axs[i // 2][i % 2].set_ylim([0, 70])
        axs[i // 2][i % 2].grid()
        axs[i // 2][i % 2].tick_params(axis='both', which='major', labelsize=16, rotation=70)
    fig.tight_layout(pad=1.0)
    plt.show()