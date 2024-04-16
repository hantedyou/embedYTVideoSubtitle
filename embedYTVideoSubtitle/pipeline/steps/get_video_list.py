from ctypes import util
import urllib.request
import json

from embedYTVideoSubtitle.pipeline.steps.step import Step, StepException
from embedYTVideoSubtitle.setting import YTDATAAPI_KEY

class GetVideoListStep(Step):
    def __init__(self):
        pass
    def process(self, data, inputs, utils):
        channel_id = inputs['channel_id']

        if utils.video_list_file_exist(channel_id):
            print(f"Video list file {channel_id} already exist")
            return self.read_file(utils.get_video_list_filespath(channel_id))

        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(YTDATAAPI_KEY, channel_id)

        video_links = []
        url = first_url

        while True:
            # Create a Request object with a User-Agent header
            req = urllib.request.Request(
                url,
                headers={
                    'User-Agent': 'Mozilla/6.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
                }
            )

            # inp = urllib.request.urlopen(url)
            # resp = json.load(inp)
            
            with urllib.request.urlopen(req) as inp:
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

        self.write_to_file(video_links, utils.get_video_list_filespath(channel_id))

        return video_links
    
    def write_to_file(self, video_links, file_path) -> None:
        with open(file_path, 'w') as f:
            for url in video_links:
                f.write(url + '\n')

    def read_file(self, file_path) -> list:
        video_links = []
        with open(file_path, 'r') as f:
            video_links.extend(url.strip() for url in f)
            # for url in f:
            #    video_links.append(url.strip())
        return video_links




