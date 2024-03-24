import os

#  處理直接執行main.py找不到embedYTVideoSubtitle問題
#  另外作法是把main.py放在d:/pythonProject/embedYTVideoSubtitle/
#  https://www.programmersought.com/article/7436148385/
import sys
sys.path.append('../')

from embedYTVideoSubtitle.steps.get_video_list import GetVideoListStep
from embedYTVideoSubtitle.steps.step import StepException


steps=[
    GetVideoListStep(),
]


for step in steps:
    try:
        step.process()
    except StepException as e:
        print('Exception: ', e)
        break

CHANNEL_ID = 'UC8butISFwT-Wl7EV0hUK0BQ' 
# video_list = get_all_video_in_channel(CHANNEL_ID)
# print(video_list)
