import os

#  處理直接執行main.py找不到embedYTVideoSubtitle問題
#  另外作法是把main.py放在d:/pythonProject/embedYTVideoSubtitle/
#  https://www.programmersought.com/article/7436148385/
import sys
sys.path.append('../')

from embedYTVideoSubtitle.pipeline.pipeline import Pipeline
from embedYTVideoSubtitle.pipeline.steps.step import StepException
from embedYTVideoSubtitle.pipeline.steps.preflight import Preflight
from embedYTVideoSubtitle.pipeline.steps.get_video_list import GetVideoListStep
from embedYTVideoSubtitle.pipeline.steps.download_subtitles import DownloadSubtitles
from embedYTVideoSubtitle.pipeline.steps.read_subtitles import ReadSubtitles
from embedYTVideoSubtitle.pipeline.steps.postflight import Postflight
from embedYTVideoSubtitle.utils import Utils

# CHANNEL_ID = 'UC8butISFwT-Wl7EV0hUK0BQ'
CHANNEL_ID = 'UCXg7gy4XmPZEGr4kumPNGyQ'  #  IELTS Advantage

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps=[
        Preflight(),
        GetVideoListStep(),
        DownloadSubtitles(),
        ReadSubtitles(),
        Postflight(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()


# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(video_list)
