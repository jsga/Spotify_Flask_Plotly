from flask import render_template, flash, redirect, url_for, request,Markup
from app import app
from app.forms import LoginForm
from utils import spotify_API, analysis

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # When the browser sends the GET request to receive the web page with the form, this method is going to return False,
    # so in that case the function skips the if statement and goes directly to render the template in the last line of the function.
    if form.validate_on_submit():

        # Gather inputs
        tokenID = form.tokenID.data

        # Fixed parameters
        limit_playlist = 30
        limit_track = 50

        # Get list from spotify
        try:
            data = spotify_API.get_audio_feat_user(tokenID, limit_playlist=limit_playlist, limit_track=limit_track)

        except ValueError as e:
            # Print error in the main dashboard
            return render_template('dashboard.html', error_text = e, form=form)

        # Call the graphic functions
        div_hist = Markup(analysis.plot_1d_features(data))
        div_scatter = Markup(analysis.plot_2d_features(data))

        # Render table
        div_data = Markup(analysis.table_features(data))

        # Render template
        return render_template('dashboard.html', div_hist=div_hist, div_scatter = div_scatter, div_data = div_data, form=form)


    # If no button is pressed

    return render_template('dashboard.html', form=form)


