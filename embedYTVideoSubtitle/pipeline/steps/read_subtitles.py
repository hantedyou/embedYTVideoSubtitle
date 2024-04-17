import os
from pprint import pprint

from embedYTVideoSubtitle.pipeline.steps.step import Step
from embedYTVideoSubtitle.setting import SUBTITLES_DIR

class ReadSubtitles(Step):
    def process(self, data, inputs, utils):
        # 儲存所有字幕(Key, Value) = (字幕標題, 字幕內容)
        data = {}

        # for test
        test_count = 0

        for subtitle_file in os.listdir(SUBTITLES_DIR):
            # for test
            if not (test_count % 50):
                print(f"Counts of subtitle files: {test_count}")
                print(f"Read subtitle_file: {subtitle_file}")
            subtitles = {}

            with open(os.path.join(SUBTITLES_DIR, subtitle_file), 'r' ,encoding='utf-8') as f:
                isTimeLine = False
                time = None
                # 儲存字幕(Key, Value) = (字幕內容, 時間)
                subtitle = None
                for line in f:
                    if '<c>' in line:
                        # 不需要分開格式的字幕，直接pass
                        continue

                    if '-->' in line:
                        # 時間
                        isTimeLine = True
                        time = line.strip()
                        continue

                    if isTimeLine:
                        # 時間下一行是要的字幕
                        subtitle = line.strip()
                        subtitles[subtitle] = time
                        isTimeLine = False
                        
        
            data[subtitle_file] = subtitles
            test_count += 1
        
        pprint(data['XMRvVcP2dPc.en.vtt'])
        return data