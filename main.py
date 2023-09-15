import requests


link = 'https://xkcd.com/614/info.0.json'
response = requests.get(link)
response.raise_for_status()
print(response.json()['alt'])
# img_link = response.json()['img']
# response_img = requests.get(img_link)
# response_img.raise_for_status()
# with open("image.png", "wb") as imagge:
#     imagge.write(response_img.content)