# Collection of plotting functions

import plotly
import plotly.graph_objs as go
import plotly.figure_factory as ff

import numpy as np
import scipy


def plot_1d_features(data):
    """
    Makes a histogram of the selected feature
    """

    # Add histogram data
    x1 = data[['acousticness']].T.squeeze()
    x2 = data[['danceability']].T.squeeze()

    # Group data together
    hist_data = [x1, x2]

    group_labels = ['Group 1', 'Group 2']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.1, .1])
    my_plot_div = plotly.offline.plot(fig, output_type='div')

    # Return as a div
    return my_plot_div




def plot_2d_features(data,feat1 = "instrumentalness",feat2 = "danceability"):
    """
    Returns a plotly object with a scatter plot of feat1 vs feat2
    """

    return None


def table_features(data):
    """
    Returns a plotly object with a data table
    """

    data_select = data[['album_name', 'artist_name','name','acousticness', 'danceability','energy','instrumentalness']]
    df_table = plotly.offline.plot(ff.create_table(data_select), output_type='div')

    return df_table


# TEST
# data = pd.read_csv('Testing_data.csv',sep='\t')