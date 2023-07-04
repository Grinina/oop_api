import requests
import os
from pprint import pprint

class Superhero:
    def get_files_list(self):
        files_url = 'https://akabab.github.io/superhero-api/api/all.json'
        response = requests.get(files_url)
        return response.json()

sh = Superhero()
data = sh.get_files_list()

count = []
result_hero_list = []
for heroes in data:
    if heroes['name'] == 'Hulk' or heroes['name'] == 'Captain America' or heroes['name'] == 'Thanos':
        result_hero_dict = {heroes['name']:heroes['powerstats']['intelligence']}
        count.append(heroes['powerstats']['intelligence'])
        result_hero_list.append(result_hero_dict)

for i in count:
    for x in result_hero_list:
        for k, v in x.items():
            if i == max(count):
                res = f'Самый умный супергерой - {k}'

print(res)

class YaUploader:
    def __init__(self, token: str):
        self.token = token
    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/v1/disk'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, filename):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": filename, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload(self, path_to_file):
        filename = os.path.basename(path_to_file)
        href = self._get_upload_link(filename=filename).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
TOKEN = 'y0_AgAAAABeP4fBAADLWwAAAADm_EAZPxPIXxs2SDKnKq33cmyFdh3-XH8'
if __name__ == '__main__':
    uploader = YaUploader(token=TOKEN)
    path_to_file = os.path.join(os.getcwd(), 'test.txt')
    uploader.upload(path_to_file)



