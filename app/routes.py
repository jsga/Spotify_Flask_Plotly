from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from utils import spotify_API

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # When the browser sends the GET request to receive the web page with the form, this method is going to return False,
    # so in that case the function skips the if statement and goes directly to render the template in the last line of the function.
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.tokenID.data, form.remember_me.data))

        # Here I could access the spotify API
        response = spotify_API.get_playlists(form.tokenID.data, form.limit.data, form.offset.data)

        # Then, to begin with, display playlists obtained
        show = ''
        for item in response['items']:
            show += item['name'] + '\n'
        return show
        #return redirect(url_for('results'))

    # If no button is pressed, simply renger the form
    return render_template('login.html', title='Sign In', form=form)


@app.route('/results')
def results():
# https://developer.spotify.com/console/get-current-user-playlists/?limit=10&offset=0

    return 'Now the results are shown!'