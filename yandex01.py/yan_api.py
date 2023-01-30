
import requests

token = "y0_AgAAAABkuGpgAADLWwAAAADRmiQicuZXszXcTha7eRudxeA0jOx_8_Y"

url = 'https://cloud-api.yandex.net/v1/disk/resources'
headers = {'Authorization': f'OAuth {token}'}


def create_folder(folder_name):
    params = {'path': folder_name}
    res = requests.put(url, headers=headers, params=params)
    return res.status_code


def get_folder_info(folder_name):
    params = {'path': folder_name}
    res = requests.get(url, headers=headers, params=params)
    return res.status_code



def delete_folder(folder_name):
    params = {'path': folder_name}
    res = requests.delete(url, headers=headers, params=params)
    return res.status_code


# if __name__ == '__main__':
#     delete_folder('test')
