from apiclient.discovery import build


class YoutubeSubscriberCount(object):
    def __init__(self, api_key = 'API_KEY '):
        self.api_key = api_key
        self.youtube = build('youtube', 'v3', developerKey=api_key)

    @property
    def get(self):
        res = self.youtube.channels().list(id="YOUTUBE_ID", part="statistics").execute()
        return res['items'][0]['statistics']['subscriberCount']

obj = YoutubeSubscriberCount()
print("As of , the current Subscriber count number is:  {}".format(obj.get))
