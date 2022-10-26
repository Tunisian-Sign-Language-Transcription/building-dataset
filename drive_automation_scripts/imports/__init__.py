from asyncio.windows_events import NULL
from operator import index
from Google import Create_Service
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
import pandas as pd
import requests
import io
import os
import gspread
import logging
import time
import sys
import json


CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive',
          'https://www.googleapis.com/auth/spreadsheets']


service, cred = Create_Service(
    CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
file = gspread.authorize(cred)


dict_folder_id = os.environ.get('DICT_FOLDER_ID')
