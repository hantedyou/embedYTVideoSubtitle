import urllib.request
import json

from embedYTVideoSubtitle.pipeline.steps.step import Step, StepException
from embedYTVideoSubtitle.setting import YTDATAAPI_KEY

class GetVideoListStep(Step):
    def __init__(self):
        pass
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(YTDATAAPI_KEY, channel_id)

        video_links = []
        url = first_url
        while True:
            inp = urllib.request.urlopen(url)
            resp = json.load(inp)

            for i in resp['items']:
                if i['id']['kind'] == "youtube#video":
                    video_links.append(base_video_url + i['id']['videoId'])

            try:
                next_page_token = resp['nextPageToken']
                url = first_url + '&pageToken={}'.format(next_page_token)
            except KeyError:
                # when there's no more page 
                break

        print(len(video_links), video_links[:5])
        return video_links





