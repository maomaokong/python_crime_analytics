#!/usr/bin/python

"""
Import packages / libraries
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

from my_config import Config as cfg
from my_config import Environment as env


def borough_color(borough):
    if borough == 'Manhattan':
        return 'green'
    elif borough == 'Brooklyn':
        return 'cyan'
    elif borough == 'Queens':
        return 'blue'
    elif borough == 'The Bronx':
        return 'red'
    elif borough == 'Staten Island':
        return 'magenta'
    else:
        return 'error'


def plot_a(df):
    main_title = 'Number of Crime per Borough'

    df0 = df.groupby('Borough')\
        .agg({'Murder': 'sum', 'Robbery': 'sum', 'Aggravated Assault': 'sum', 'Property Crime Total': 'sum'})\
        .reset_index()
    #print()
    #print(df1)

    fig1 = plt.figure(1)

    a = df0['Borough']
    b = df0['Murder']
    c = df0['Robbery']
    d = df0['Aggravated Assault']
    e = df0['Property Crime Total']

    ax1 = plt.subplot(2, 2, 1)
    ax1.set_title('Murder', fontdict={'fontweight': 'bold'})
    ax1.yaxis.grid(True)
    plt.plot(
        a, b,
        color='green',
        linestyle='-',
        linewidth=2,
        marker='o',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = plt.subplot(2, 2, 2, sharex=ax1)
    ax2.set_title('Robbery', fontdict={'fontweight': 'bold'})
    ax2.yaxis.grid(True)
    plt.plot(
        a, c,
        color='cyan',
        linestyle='--',
        linewidth=2,
        marker='v',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax2.get_xticklabels(), visible=False)

    ax3 = plt.subplot(2, 2, 3, sharex=ax1)
    ax3.set_title('Aggravated Assault', fontdict={'fontweight': 'bold'})
    ax3.yaxis.grid(True)
    plt.plot(
        a, d,
        color='blue',
        linestyle='-.',
        linewidth=2,
        marker='D',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax3.get_xticklabels())

    ax4 = plt.subplot(2, 2, 4, sharex=ax1)
    ax4.set_title('Property Crime', fontdict={'fontweight': 'bold'})
    ax4.yaxis.grid(True)
    plt.plot(
        a, e,
        color='red',
        linestyle=':',
        linewidth=2,
        marker='s',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax4.get_xticklabels())

    fig1.tight_layout()
    fig1.suptitle(main_title, fontsize=18, fontweight='bold')

    fig_mgr = plt.get_current_fig_manager()
    fig_mgr.window.showMaximized()

    plt.subplots_adjust(top=0.9)
    plt.show()


def plot_b(df):
    main_title = '% vs Borough Population'

    df['Murder_Perc'] = df['Murder'] / df['Population'] * 100
    df['Robbery_Perc'] = df['Robbery'] / df['Population'] * 100
    df['Aggravated_Assault_Perc'] = df['Aggravated Assault'] / df['Population'] * 100
    df['Property_Crime_Perc'] = df['Property Crime Total'] / df['Population'] * 100
    #print()
    #print(df)

    df0 = df.groupby('Borough')\
        .agg(\
        {
            'Murder_Perc': 'mean',
            'Robbery_Perc': 'mean',
            'Aggravated_Assault_Perc': 'mean',
            'Property_Crime_Perc': 'mean'
        }\
        )\
        .reset_index()
    #print()
    #print(df0)

    fig2 = plt.figure(2)

    a = df0['Borough']
    b = df0['Murder_Perc']
    c = df0['Robbery_Perc']
    d = df0['Aggravated_Assault_Perc']
    e = df0['Property_Crime_Perc']

    ax1 = plt.subplot(2, 2, 1)
    ax1.set_title('Murder%', fontdict={'fontweight': 'bold'})
    ax1.yaxis.grid(True)
    ax1.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.plot(
        a, b,
        color='green',
        linestyle='-',
        linewidth=2,
        marker='o',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax1.get_xticklabels(), visible=False)

    ax2 = plt.subplot(2, 2, 2, sharex=ax1)
    ax2.set_title('Robbery%', fontdict={'fontweight': 'bold'})
    ax2.yaxis.grid(True)
    ax2.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.plot(
        a, c,
        color='cyan',
        linestyle='--',
        linewidth=2,
        marker='v',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax2.get_xticklabels(), visible=False)

    ax3 = plt.subplot(2, 2, 3, sharex=ax1)
    ax3.set_title('Aggravated Assault%', fontdict={'fontweight': 'bold'})
    ax3.yaxis.grid(True)
    ax3.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.plot(
        a, d,
        color='blue',
        linestyle='-.',
        linewidth=2,
        marker='D',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax3.get_xticklabels())

    ax4 = plt.subplot(2, 2, 4, sharex=ax1)
    ax4.set_title('Property Crime%', fontdict={'fontweight': 'bold'})
    ax4.yaxis.grid(True)
    ax4.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
    plt.plot(
        a, e,
        color='red',
        linestyle=':',
        linewidth=2,
        marker='s',
        markersize=10,
        markerfacecolor='black',
        markeredgecolor='black'
    )
    plt.setp(ax4.get_xticklabels())

    fig2.tight_layout()
    fig2.suptitle(main_title, fontsize=18, fontweight='bold')

    fig_mgr = plt.get_current_fig_manager()
    fig_mgr.window.showMaximized()

    plt.subplots_adjust(top=0.9)
    plt.show()


def plot_c(df):
    main_title = 'Number of Murder per Borough'

    fig3 = plt.figure(3)

    ax_ind = 1
    for borough, subdf in df.groupby('Borough'):
        years = subdf['Year'].values
        murder = subdf['Murder'].values

        ax = plt.subplot(3, 2, ax_ind)
        plt.plot(
            years, murder,
            color='red',
            linestyle='-',
            linewidth=2,
            marker='o',
            markersize=10,
            markerfacecolor='black',
            markeredgecolor='black'
        )
        ax.set_title(borough, fontdict={'fontweight': 'bold'})
        ax.set_xticks(np.arange(min(years), max(years)+1))
        ax.yaxis.grid(True)
        ax_ind += 1

    fig3.tight_layout()
    fig3.suptitle(main_title, fontsize=18, fontweight='bold')

    fig_mgr = plt.get_current_fig_manager()
    fig_mgr.window.showMaximized()

    plt.subplots_adjust(top=0.9)
    plt.show()


def plot_d(df):
    year_min = df['Year'].values.min()
    year_max = df['Year'].values.max()

    main_title = 'Crime Types Trends between {0} and {1}'.format(year_min, year_max)

    selected_years = [year_min, year_max]
    #print(selected_years)

    # select data in selected_years: df[df['Year'].isin(selected_years)]
    # select data not in selected_years: df[~df['Year'].isin(selected_years)]
    df0 = df[df['Year'].isin(selected_years)]
    #print(df0[['Borough', 'Year', 'Murder']])

    fig4 = plt.figure(4, figsize=(12, 4))

    xax = 1
    for borough, subdf in df0.groupby('Borough'):
        #print(subdf)

        # Get Murder 2010 and 2014 values
        borough_murder_2010 = subdf.query('Year == ' + str(year_min))['Murder'].values
        borough_murder_2014 = subdf.query('Year == ' + str(year_max))['Murder'].values
        #print("[{0}] {1}: {2} >> {3}".format(year_min, borough, borough_murder_2010, borough_murder_2014))

        # Set up the x-axis values
        x1 = xax - 0.2
        x2 = xax + 0.2

        # Get line colors
        line_colors = borough_color(borough)

        ax = plt.subplot(1, 5, 1)
        ax.plot(
            [x1, x2], [borough_murder_2010, borough_murder_2014],
            color=line_colors,
            linewidth=2
        )
        ax.set_title('Murder', fontdict={'fontweight': 'bold'})
        ax.set_xticklabels([])
        ax.yaxis.grid(True)

        # Get Robbery 2010 and 2014 values
        borough_robbery_2010 = subdf.query('Year == ' + str(year_min))['Robbery'].values
        borough_robbery_2014 = subdf.query('Year == ' + str(year_max))['Robbery'].values
        #print("[{0}] {1}: {2} >> {3}".format(year_min, borough, borough_robbery_2010, borough_robbery_2014))

        ax = plt.subplot(1, 5, 2)
        ax.plot(
            [x1, x2], [borough_robbery_2010, borough_robbery_2014],
            color=line_colors,
            linewidth=2
        )
        ax.set_title('Robbery', fontdict={'fontweight': 'bold'})
        ax.set_xticklabels([])
        ax.yaxis.grid(True)

        # Get Assault 2010 and 2014 values
        borough_assault_2010 = subdf.query('Year == ' + str(year_min))['Aggravated Assault'].values
        borough_assault_2014 = subdf.query('Year == ' + str(year_max))['Aggravated Assault'].values

        ax = plt.subplot(1, 5, 3)
        ax.plot(
            [x1, x2], [borough_assault_2010, borough_assault_2014],
            color=line_colors,
            linewidth=2
        )
        ax.set_title('Aggravated Assault', fontdict={'fontweight': 'bold'})
        ax.set_xticklabels([])
        ax.yaxis.grid(True)

        borough_propery_2010 = subdf.query('Year == ' + str(year_min))['Property Crime Total'].values
        borough_propery_2014 = subdf.query('Year == ' + str(year_max))['Property Crime Total'].values

        ax = plt.subplot(1, 5, 4)
        ax.plot(
            [x1, x2], [borough_propery_2010, borough_propery_2014],
            color=line_colors,
            linewidth=2
        )
        ax.set_title('Property Crime', fontdict={'fontweight': 'bold'})
        ax.set_xticklabels([])
        ax.yaxis.grid(True)

    # Legend
    manhattan_line = mlines.Line2D([], [], color=borough_color('Manhattan'), label='Manhattan')
    brooklyn_line = mlines.Line2D([], [], color=borough_color('Brooklyn'), label='Brooklyn')
    queens_line = mlines.Line2D([], [], color=borough_color('Queens'), label='Queens')
    bronx_line = mlines.Line2D([], [], color=borough_color('The Bronx'), label='The Bronx')
    staten_line = mlines.Line2D([], [], color=borough_color('Staten Island'), label='Staten Island')

    fig4.tight_layout()
    fig4.suptitle(main_title, fontsize=18, fontweight='bold')
    fig4.legend(handles=[brooklyn_line, bronx_line, queens_line, manhattan_line, staten_line], loc='upper right')

    fig_mgr = plt.get_current_fig_manager()
    fig_mgr.window.showMaximized()

    plt.subplots_adjust(top=0.9)
    plt.show()


def main():
    if cfg.ENV == env.UAT:
        print()
        print("# Crime Rate's Data Analytics is running in UAT environment!")
    elif cfg.ENV == env.PROD:
        print()
        print("# Crime Rate's Data Analytics is running in PROD environment!")
        #print("## This will take more longer time to runt the application!!")

    crime_data = "{0}/{1}/{2}/{3}".format(cfg.PATH_PARENT, cfg.PATH_DATA, cfg.PATH_DATA_INPUT, cfg.INPUT_CRIME_DATA)
    #print()
    #print(crime_data)
    df = pd.read_csv(crime_data)
    #print()
    #print(df.head())

    plot_a(df)

    plot_b(df)

    plot_c(df)

    plot_d(df)


if __name__ == '__main__':
    main()

