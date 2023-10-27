import random
import os
import requests

from dotenv import load_dotenv


def download_comic(link, path):
    response = requests.get(link)
    response.raise_for_status()
    comic = response.json()
    picture_url = comic['img']
    picture_response = requests.get(picture_url)
    picture_response.raise_for_status()
    with open(path, 'wb') as image:
        image.write(picture_response.content)
    return comic['alt']


def check_response(response):
    vk_response = response.json()
    if 'error' in vk_response:
        raise Exception('token_error')
    else:
        return vk_response


def get_wall_upload_server(token, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    params = {
        'access_token': token,
        'group_id': group_id,
        'v': '5.150'
    }
    vk_response = requests.get(url, params=params)
    vk_response.raise_for_status()
    upl_server = check_response(vk_response)
    return upl_server['response']['upload_url']


def upload_photo(path, link):
    with open(path, 'rb') as image:
        files = {
            'photo': image
        }
        response = requests.post(link, files=files)
    response.raise_for_status()
    image_info = response.json()
    return image_info


def save_photo(token, group_id, hash_id, server, photo):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    params = {
        'group_id': group_id,
        'hash': hash_id,
        'server': server,
        'photo': photo,
        'access_token': token,
        'v': '5.154'
    }

    response = requests.post(url, params=params)
    response.raise_for_status()
    save_response = check_response(response)
    return save_response['response']


def post_wall_photo(token, group_id, attachments, message):
    url = 'https://api.vk.com/method/wall.post'
    params = {
        'access_token': token,
        'v': '5.154'
    }
    payload = {
        'owner_id': f'-{group_id}',
        'attachments': attachments,
        'message': message
    }
    response = requests.post(url, params=params, data=payload)
    response.raise_for_status()
    save_response = check_response(response)
    return save_response['response']


if __name__ == '__main__':
    max_comic_number = 2839
    comics_number_range = random.randint(1, max_comic_number)
    link = f'https://xkcd.com/{comics_number_range}/info.0.json'
    load_dotenv()
    vk_access_token = os.environ['VK_ACCESS_TOKEN']
    vk_group_id = os.environ['VK_GROUP_ID']

    try:
        upload_server = get_wall_upload_server(vk_access_token, vk_group_id)
        upload_url = upload_server

        message = download_comic(link, 'comic.png')

        upl_photo = upload_photo('comic.png', upload_url)
        server_id = upl_photo['server']
        photo_id = upl_photo['photo']
        hash_ = upl_photo['hash']

        photo_response = photo_response(vk_access_token, vk_group_id, hash_, server_id, photo_id)
        attachments = f"photo{photo_response[0]['owner_id']}_{photo_response[0]['id']}"
        post_response = post_wall_photo(vk_access_token, vk_group_id, attachments, message)
    finally:
        os.remove('comic.png')
