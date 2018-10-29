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

    group_labels = ['Acousticness', 'Danceability']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(hist_data, group_labels, bin_size=[.05, .05])
    my_plot_div = plotly.offline.plot(fig, output_type='div')

    # Return as a div
    return my_plot_div




def plot_2d_features(data):
    """
    Returns a plotly object with a scatter plot of feat1 vs feat2
    """

    # Create a trace
    trace = go.Scatter(
        x=data[['acousticness']].T.squeeze(),
        y = data[['danceability']].T.squeeze(),
        mode='markers',
        marker = dict(
            size=16,
            color=data[['energy']].T.squeeze(),  # set color equal to a variable
            colorscale='RdBu',
            showscale=True),
        text = data[['name']].T.squeeze()
    )

    layout = go.Layout(
        title='',#''Acousticness vs danceability index. Color represents energy of the track.',
        hovermode='closest',
        xaxis=dict(
            title='Acousticness'
        ),
        yaxis=dict(
            title='Danceability'
        )
    )

    fig = go.Figure(data=[trace], layout=layout)
    my_plot_div = plotly.offline.plot(fig, output_type='div')

    # Return as a div
    return my_plot_div



def table_features(data):
    """
    Returns a plotly object with a data table
    """

    data_select = data[['album_name', 'artist_name','name','acousticness', 'danceability','energy','instrumentalness']]
    df_table = plotly.offline.plot(ff.create_table(data_select), output_type='div')

    return df_table

