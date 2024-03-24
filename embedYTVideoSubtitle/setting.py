from dotenv import load_dotenv
import os

#  import environmet variables from .env file
load_dotenv()
YTDATAAPI_KEY = os.getenv('YTDATAAPI_KEY')  #  read environmet variables