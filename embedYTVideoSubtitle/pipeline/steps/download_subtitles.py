import os
import time

import yt_dlp

from embedYTVideoSubtitle.pipeline.steps.step import Step, StepException 
from embedYTVideoSubtitle.setting import SUBTITLES_DIR
from embedYTVideoSubtitle.utils import Utils

class DownloadSubtitles(Step):
    def __init__(self):
        pass

    def process(self, data, inputs, utils):
        """
            data: video urls
        """
        print("start download subtitles")
        print("Counts of video urls: ", len(data))

        # count for pass download
        pass_count = 0
       
        subtitle_path = SUBTITLES_DIR
        subtitle_ext = '*.vtt'  # For example, to find all .vtt subtitle files
        # 已下載字幕檔，含完整路徑
        matched_filenames = utils.find_files_with_pattern(subtitle_path, subtitle_ext)
        print(f"Length of matched_filenames:{len(matched_filenames)}")


        #  self-defined template of subtitles filename
        subtitle_pattern = utils.get_subtile_file_path('%(id)s.%(ext)s')
        ydl_opts = {
            'writesubtitles': True,
            'writeautomaticsub': True,
            'skip_download': True,
            'subtitleslangs': ['en'],
            'outtmpl': {
                'subtitle': subtitle_pattern  # Apply the template for subtitles
                },
            }
        


        start = time.time()

        # 測試用，避免重複下載太多次
        test_count = 0

        for url in data:
            # Extract video ID from the URL
            video_id = url.split('v=')[-1]
            # Predict the subtitle filename based on the video ID and the template
            predicted_subtitle_filename = subtitle_pattern.replace('%(id)s', video_id).replace('%(ext)s', 'en.vtt')
            # print(f"predicted_subtitle_filename:{predicted_subtitle_filename}")

            # if os.path.exists(predicted_subtitle_filename):
            if predicted_subtitle_filename in matched_filenames:
                pass_count += 1
                # print(f"Subtitle file {predicted_subtitle_filename} already exists.")
                continue

            test_count += 1
            print(f"Test count: {test_count}")

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # download subtitles
                # ydl.download([url])
                result = ydl.extract_info(url, download=True)
                subtitle_filename = result.get('subtitle')
                # print(f"Expected subtitle filename: {subtitle_filename}")

            # 測試用，避免重複下載太多次
            if test_count >= 10:
                break            

        end = time.time()
        print(f"Counts of pass download: {pass_count}")
        print(f"Subtitles download time: {end - start}")
