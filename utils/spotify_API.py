import requests

# Get a list of playlist from current user
# https://developer.spotify.com/console/get-current-user-playlists/?limit=10&offset=5


def get_playlists(tokenID,limit=10,offset=0):

    # This is a nice help: to write down parameters
    # https://curl.trillworks.com/

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

    # END
    return response.json()


# TEST
# tokenID = 'BQBR3qkIoCmt8cpP1B2uuvfv-6z6B2Zen46UN3LPh6oVeY0E6QNBXCMSD5e7pvC68ye4wKktodRlZPiS3uN7KLpbcr-Bq7w0WqPc5D2Hpc0ehN7cD4eIuitwj9dc0KYdFKkiOjPpJ0g2X12ozcOojDl6xyK_Pa8xKK1u-YGpOFbv2SblldI'
# limit = 10
# offset = 0
# response = get_playlists(tokenID, limit, offset)
# print(response)
# show = ""
# for item in response['items']:
#     #print("%d %s" % (i, item['name']))
#     show += item['name'] + '\n'
# print(show)





# Then, for each playlist, get a list of the tracks
# https://developer.spotify.com/console/get-playlist-tracks/

# For a track, return features
# https://developer.spotify.com/console/get-audio-features-several-tracks/


