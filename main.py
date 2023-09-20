from dotenv import load_dotenv

import os
import requests


link = 'https://xkcd.com/614/info.0.json'
response = requests.get(link)
response.raise_for_status()
load_dotenv()
client_id = os.environ['CLIENT_ID']
access_token = os.environ['ACCESS_TOKEN']
group_id = os.environ['GROUP_ID']
vk_response = requests.get(f'https://api.vk.com/method/photos.getWallUploadServer?&access_token={access_token}&group_id={group_id}&v=5.150')
vk_response.raise_for_status()
print(vk_response.json())

# #"response": {
# "album_id": -14,
# "upload_url": "https://pu.vk.com...i=1&wallphoto=1",
# "user_id": 715752416