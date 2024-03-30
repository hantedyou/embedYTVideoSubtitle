from dotenv import load_dotenv
import os

#  import environmet variables from .env file
load_dotenv()
YTDATAAPI_KEY = os.getenv('YTDATAAPI_KEY')  #  read environmet variables


DOWNLODADS_DIR = 'downloads'
VIDEOS_DIR = os.path.join(DOWNLODADS_DIR, 'videos')
SUBTITLES_DIR = os.path.join(DOWNLODADS_DIR,'subtitles')

