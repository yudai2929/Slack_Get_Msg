import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SLACK_CHANNEL_ID = os.environ.get('SLACK_CHANNEL_ID')
SLACK_URL = os.environ.get('SLACK_URL')
TOKEN = os.environ.get('TOKEN')

