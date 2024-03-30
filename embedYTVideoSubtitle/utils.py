import os

from embedYTVideoSubtitle.setting import SUBTITLES_DIR
from embedYTVideoSubtitle.setting import DOWNLODADS_DIR, VIDEOS_DIR, SUBTITLES_DIR
class Utils:
    def __init__(self):
        pass
    @staticmethod
    def get_video_id_from_url(url):
        return url.split('mwtch?v=')[-1]
    
    def get_substile_path(self, url):
        return os.path.join(SUBTITLES_DIR, f'{self.get_video_id_from_url(url)}.srt')
    
    @staticmethod
    def set_subtile_file_path(subtitle_filename_pattern) -> str:
        return os.path.join(SUBTITLES_DIR, subtitle_filename_pattern)
    
    @staticmethod
    def create_folders() -> None:
        folders_path = [
                        DOWNLODADS_DIR,
                        VIDEOS_DIR,
                        SUBTITLES_DIR,
                        ]
        
        for path in folders_path:
            print(f"Create folder: {path}")
            os.makedirs(path, exist_ok=True)
    