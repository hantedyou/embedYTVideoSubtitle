from ctypes import util
import os

import yt_dlp

from embedYTVideoSubtitle.pipeline.steps.step import Step, StepException 
from embedYTVideoSubtitle.setting import SUBTITLES_DIR

class DownloadSubtitles(Step):
    def __init__(self):
        pass
    def process(self, data, inputs, utils):
        """
            data: video urls
        """
        print("start download subtitles")
        print("Counts of video urls: ", len(data))
        
        #  self-defined template of subtitles filename
        #  output_template = '%(title)s-%(id)s.%(ext)s'
        subtitle_pattern = utils.set_subtile_file_path('%(id)s.%(ext)s')

        for url in data:
            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'skip_download': True,
                'subtitleslangs': ['en'],
                'outtmpl': {
                    'subtitle': subtitle_pattern  # Apply the template for subtitles
                    },
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # download subtitles
                ydl.download([url])
                result = ydl.extract_info(url, download=True)
            
            # print(f"Expected subtitle filename: {subtitle_filename}")
            break
