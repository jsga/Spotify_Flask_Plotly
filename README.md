This is a simple flask app that uses the Spotify API to:

1. Collect playlists from the current user
2. Collect the tracks from all the playlists
3. Gather the audio features from all tracks
4. Displays interactive visualizations with summary values from the audio features

The app is based on Flask and a single-paged [flexbox](https://www.w3schools.com/css/css3_flexbox.asp). The Api calls and the plots are made in Python 3 and the visualizations are produced with Plotly figures.

![App](https://github.com/jsga/Spotify_Flask_Plotly/blob/master/Screenshots/Screenshot_App.png)

## How to run it locally

```
git clone https://github.com/jsga/Spotify_Flask_Plotly.git
cd Spotify_Flask_Plotly
sh start.sh
```
Then visit http://127.0.0.1:5000/, press Ctrl + C to quit

## How to get a valid token

Go to [Spotify for developers](https://developer.spotify.com/console/get-current-user-playlists/) website and press _"Get Token"_. The required scopes for the endpoint uses are "playlist-read-private".

![Spotify screenshot](https://github.com/jsga/Spotify_Flask_Plotly/blob/master/Screenshots/Screenshot_Spotify.png)

## What do the audio features mean?

- Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
- Acousticness: A measure from 0.0 to 1.0 of whether the track is acoustic.
- Energy: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.
- A complete list of the features is described in [this](https://medium.com/@boplantinga/what-do-spotifys-audio-features-tell-us-about-this-year-s-eurovision-song-contest-66ad188e112a) post.

## Todo list

- Allow the user to select which features to show
- Divide the analysis in multiple pages
