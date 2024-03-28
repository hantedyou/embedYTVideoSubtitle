import yt_dlp

#  from traceback import print_tb
#  from pytube import YouTube

from embedYTVideoSubtitle.pipeline.steps.step import Step, StepException 


class DownloadSubtitles(Step):
    def __init__(self):
        pass
    def process(self, data, inputs):
        """
            data: video urls
        """
        print("start download subtitles")
        print("Length of video urls: ", len(data))
        cnt = 0
        
        # self-defined template of subtitles filename
        output_template = '%(title)s-%(id)s.%(ext)s'

        for url in data:
            ydl_opts = {
                'writesubtitles': True,
                'writeautomaticsub': True,
                'skip_download': True,
                'subtitleslangs': ['en'],
                'outtmpl': {
                    'subtitle': output_template  # Apply the template for subtitles
                    },
                }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # download subtitles
                # ydl.download([url])
                result = ydl.extract_info(url, download=True)
                subtitle_filename = f"{result['title']}-{result['id']}.en.vtt"
            
            print(f"Expected subtitle filename: {subtitle_filename}")
            break