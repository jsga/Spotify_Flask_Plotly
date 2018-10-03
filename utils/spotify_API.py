import requests
import pandas as pd


def get_playlists(tokenID, limit=50, offset=0):
    """
    Gathers the playlists from the current user
    https://developer.spotify.com/console/get-current-user-playlists/?limit=10&offset=5
    """

    # This is a nice little help to write down parameters https://curl.trillworks.com/
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': "'Bearer " + str(tokenID) + "'"
    }

    params = (
        ('limit', limit),
        ('offset', offset),
    )

    response = requests.get('https://api.spotify.com/v1/me/playlists', headers=headers, params=params)

    if response.status_code != 200:
        raise ValueError('Error code ' + str(response.status_code) + '\n'+ str(response.json()))

    # Keep only the info we need: ID of track and name
    playlist_info = []
    for item in response.json()['items']:
        playlist_info.append({'id':item['id'] , 'name': item['name']})

    # END
    return playlist_info




def get_tracks_playlists(tokenID, playlist_info,limit=50,offset=0):
    """
    Returns a big list with the tracks from the playlists
    playlist_info is a dictionary, returned from get_playlists()
    The keys are the IDs of the playlists

    https://developer.spotify.com/console/get-playlist-tracks/
    """

    # Keep names and ID's
    track_info = []

    for pID in playlist_info:

        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': "'Bearer " + str(tokenID) + "'"
        }

        params = (
            ('market','ES'), # By default use Spanish market
            ('fields', 'items(track(name,id,album))'), # keep only the ID and the name of the song
            ('limit', limit),
            ('offset', offset),
        )

        URL_API = 'https://api.spotify.com/v1/playlists/{id}/tracks'.format(id = pID['id'])
        response = requests.get(URL_API, headers=headers, params=params)

        if response.status_code != 200:
            raise ValueError('Error code ' + str(response.status_code) + '\n' + str(response.json()))

        # Add new ID's to dic with name
        for item in response.json()['items']:
            track_info.append( {'id': item['track']['id'] ,
                                'name': item['track']['name'],
                                'album_name': item['track']['album']['name'],
                                'artist_name':item['track']['album']['artists'][0]['name']
                                })

    # END
    return track_info




def get_audio_features(tokenID, track_info):
    """
    For a list of tracks IDs, return features
    https://developer.spotify.com/console/get-audio-features-several-tracks/

    The maximum number of IDs per call is 100
    """


    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': "'Bearer " + str(tokenID) + "'"
    }


    # Concatenate all IDs
    # The maximum umber of IDs per call is 100. In that case we split them
    ids_all = [""] # keep here the list of IDs
    count = 0
    for d in track_info:
        ids_all[-1] += d['id'] + ','
        count += 1
        if count >50:
            # print('Reached 100, new call')
            ids_all.append('')
            count = 0

    # Loop every group of IDs and keep audio feat inside a pandas dataframe
    data = pd.DataFrame()
    for ids in ids_all:

        params = (('ids', ids),)

        response = requests.get('https://api.spotify.com/v1/audio-features', headers=headers, params=params)

        # Add to ID's the new fields
        data_aux = pd.DataFrame(response.json()['audio_features'])
        data = data.append(data_aux,ignore_index=True)

    # Merge now with the name of the tracks. Return a pandas DF
    track_info_pd = pd.DataFrame(track_info)
    result =  pd.concat([data, track_info_pd], axis=1, join='inner')

    return result



def get_audio_feat_user(tokenID,limit_track=50,limit_playlist = 10):
    """
    Wraps the functions that:
    - Gather playlists from current user
    - Gets tracks from all playlists
    - Gets audio features from tracks

    Returns a pandas dataframe
    """

    # Get playlists from current user
    playlist_info = get_playlists(tokenID, limit = limit_playlist, offset = 0)

    # get track list
    track_info = get_tracks_playlists(tokenID, playlist_info, limit=limit_track, offset=0)

    # Get audio features
    audioFeat = get_audio_features(tokenID, track_info)

    return audioFeat


#### TEST AREA

#
# tokenID = ''
# limit = 10
# offset = 0
# playlist_info = get_playlists(tokenID, limit, offset)
# print(playlist_info)
#
#
# # get track list
# track_info = get_tracks_playlists(tokenID,playlist_info,limit=50,offset=0)
# track_info
# len(track_info)
#
# # Get audio features
# audioF = get_audio_features(tokenID, track_info)
# #
# try:
#     tokenID = 'BQBCDI5hrLgF_HnrH9RoDKC-1m00yB9pw0ZS77mJHqPq-zOQkcDrre5NRabVwsAOp3mmnkx9XBsoloHcUKc8rTQiVifIuFhAHe4D3MifdsqNZ5qVRUlZ-_4UeIxvEYpq-CJr1664wKLQI6okEOXMlBOg-IZB33VoHFBS9pVxQiRcSu1p-OtrpE2uNWRamQ'
#     data = get_audio_feat_user(tokenID,50,10)
# except ValueError as e:
#     print(e)

# data.describe()
#
# # Save data as a csv, for later testings
# data.to_csv('Testing_data.csv', sep='\t')