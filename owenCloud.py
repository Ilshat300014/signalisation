import requests
import json

login = 'ilshatkhabriev@yandex.ru'
password = 'iserekkerpe19'
main_url = 'https://api.owencloud.ru/v1/'

def get_token(login, password):
    link = 'auth/open'
    data = json.dumps({
            "login": login,
            "password": password
        })
    req = requests.post(url=main_url + link, data=data)
    answer = json.loads(req.text)
    token = answer["token"]
    return "Bearer " + token

def get_device_info(token):
    link = 'device/index'
    header = {
        'Authorization': token
    }
    req = requests.post(url=main_url + link, headers=header)
    answer = json.loads(req.text)[0]
    return answer

def get_last_data(token, device_id):
    link = f'device/{device_id}'
    header = {
        'Authorization': token
    }
    req = requests.post(url=main_url + link, headers=header)
    answer = json.loads(req.text)
    return answer


if __name__ == '__main__':
    token = get_token(login, password)
    device_info = get_device_info(token)
    device_id = device_info['id']
    last_data = get_last_data(token, device_id)
    for i in last_data['parameters']:
        print(f"{i['code']} = {i['value']}")
        # print(i) 

# https://api.owencloud.ru/v1/object/action.
# https://web.owencloud.ru/site/login