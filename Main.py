# klucz do api: AIzaSyC-P1MowO2PRlCAlgr3pZZ8D4KF-oIZcMs

import requests
import json

API_KEY = 'AIzaSyC-P1MowO2PRlCAlgr3pZZ8D4KF-oIZcMs'
URL = 'https://www.googleapis.com/youtube/v3/videos'
PLAYLIST_URL = 'https://www.googleapis.com/youtube/v3/playlistItems'
PARAMS = {
    'part': 'snippet,contentDetails,status',
    'key': API_KEY
}


def get_video_data(video_id):
    r = requests.get(URL, params={**PARAMS, 'id': video_id})
    x = json.loads(r.text)
    print('youtube video id:', x['items'][0]['id'])


# Maximum number of results = 50
# If there are more results, there's a 'nextPageToken' in the result
# use it as 'pageToken' parameter in the request
def get_video_ids_from_playlist(playlist_id):
    r = requests.get(PLAYLIST_URL, params={**PARAMS, 'playlistId': playlist_id,
                                           'maxResults': 50, 'pageToken': 'CDIQAA'})
    playlist = json.loads(r.text)
    print(playlist['items'][0])
    print(playlist['nextPageToken'])

#get_video_data('7lCDEYXw3mM')
get_video_ids_from_playlist('PLlJLQiVVXAD_Qg_4j58ZzqJDDAE3miL5F')