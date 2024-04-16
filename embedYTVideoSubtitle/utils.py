import os
import glob

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
    def get_subtile_file_path(subtitle_filename_pattern) -> str:
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
    
    def subtitle_file_exist(self, url) -> bool:
        path = self.get_subtile_path(url)
        os.path.exists(path) and os.path.getsize(path) > 0

    @staticmethod
    def find_files_with_pattern(path, pattern) -> set:
        """
            Get files' names in a given path with a given pattern
            Since set comparison is O(1), it's faster than list
        """
        full_pattern = os.path.join(path, pattern)
        files = glob.glob(full_pattern)
        return set(files)
        # full_pattern = os.path.join(path, pattern)
        # files = glob.glob(full_pattern)
        # return {os.path.basename(file) for file in files}
    
    @staticmethod
    def find_files_set_with_pattern(path, pattern) -> set:
        """
            Get files' names in a given path with a given pattern
            Since set comparison is O(1), it's faster than list
        """
        full_pattern = os.path.join(path, pattern)
        files = glob.glob(full_pattern)
        return {os.path.basename(file) for file in files}

    def get_video_list_filespath(self, channel_id) -> str:
        """
            Get the path of the video list file
        """
        return os.path.join(DOWNLODADS_DIR, f'{channel_id}.txt')
    
    def video_list_file_exist(self, channel_id) -> bool:
        path = self.get_video_list_filespath(channel_id)
        return os.path.exists(path) and os.path.getsize(path) > 0