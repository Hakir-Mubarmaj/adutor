from googleapiclient.discovery import build
import webbrowser

def youtubesearch(query):
    api_key = 'AIzaSyBrkzHWk5DGTut-9u5nEZT9s_Rd_Ju7kp4'
    youtube = build('youtube', 'v3', developerKey=api_key)

    request = youtube.search().list(
        part='snippet',
        maxResults=1,
        q=query
    )

    response = request.execute()

    video_id = response['items'][0]['id']['videoId']
    watch_url = f'https://www.youtube.com/watch?v={video_id}'

    webbrowser.open_new(watch_url)
