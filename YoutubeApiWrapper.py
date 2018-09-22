import requests
import json

API_KEY = 'AIzaSyC-P1MowO2PRlCAlgr3pZZ8D4KF-oIZcMs'
PLAYLIST_URL = 'https://www.googleapis.com/youtube/v3/playlistItems'
PARAMS = {
    'part': 'contentDetails',
    'key': API_KEY
}


def get_video_ids_from_playlist(playlist_id, next_page=''):
    r = requests.get(PLAYLIST_URL, params={**PARAMS, 'playlistId': playlist_id,
                                           'maxResults': 50, 'pageToken': next_page})
    playlist = json.loads(r.text)

    video_ids = [item['contentDetails']['videoId'] for item in playlist['items']]
    next_page_token = playlist['nextPageToken'] if 'nextPageToken' in playlist else None

    return video_ids + get_video_ids_from_playlist(playlist_id, next_page_token) \
        if next_page_token else video_ids
