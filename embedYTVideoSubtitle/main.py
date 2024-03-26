import os

#  處理直接執行main.py找不到embedYTVideoSubtitle問題
#  另外作法是把main.py放在d:/pythonProject/embedYTVideoSubtitle/
#  https://www.programmersought.com/article/7436148385/
import sys
sys.path.append('../')

from embedYTVideoSubtitle.pipeline.pipeline import Pipeline
from embedYTVideoSubtitle.pipeline.steps.get_video_list import GetVideoListStep
from embedYTVideoSubtitle.pipeline.steps.step import StepException

CHANNEL_ID = 'UC8butISFwT-Wl7EV0hUK0BQ' 

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }

    steps=[
        GetVideoListStep(),
    ]

    p = Pipeline(steps)
    p.run(inputs)




if __name__ == '__main__':
    main()


# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(video_list)
