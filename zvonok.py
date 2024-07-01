import requests
from time import sleep

# Полная и актуальная документация по API: https://calltools.ru/guide_api


CALLTOOLS_PUBLIC_KEY = 'test_public_key'
CALLTOOLS_BASE_URL = 'https://zvonok.com'
CALLTOOLS_TIMEOUT = 40


class CallToolsException(Exception):
    pass


def create_call(campaign_id, phonenumber, text=None, speaker='Tatyana'):
    '''
    Создание звонка на прозвон с генерацией ролика
    :type campaign_id: int
    :type phonenumber: str
    :type text: str|None
    :type speaker: str
    :rtype: dict
    '''

    # https: // zvonok.com / manager / cabapi_external / api / v1 / phones / calls_by_phone /?campaign_id = 2085175147 & phone = %2
    # B79934212040 & public_key = a457c770b46296486b078f00f4ff444f
    resp = requests.post(CALLTOOLS_BASE_URL + '/manager/cabapi_external/api/v1/phones/call/', {
        'public_key': 'a457c770b46296486b078f00f4ff444f',
        'phone': phonenumber,
        'campaign_id': campaign_id,
        'text': text,
        'speaker': speaker,
    }, timeout=CALLTOOLS_TIMEOUT)
    ret = resp.json()
    # print(ret)
    # if ret['status'] == 'error':
    #     raise CallToolsException(ret['data'])
    return ret

def get_call_result(campaign_id, phonenumber,):
    resp = requests.get(CALLTOOLS_BASE_URL + '/manager/cabapi_external/api/v1/phones/calls_by_phone', {
        'public_key': 'a457c770b46296486b078f00f4ff444f',
        'phone': phonenumber,
        'campaign_id': campaign_id,
    }, timeout=CALLTOOLS_TIMEOUT)
    # ret = resp.json()
    # print(ret)
    # if ret['status'] == 'error':
    #     raise CallToolsException(ret['data'])
    return resp

if __name__ == '__main__':
    res = create_call(2085175147, '+79991642504', 'Нет связи с модемом')
    print(res)
    # sleep(20)
    # res = create_call(2085175147, '+79297206193', 'Нет связи с модемом')
    # print(res)
    calls_info = get_call_result(2085175147, '+79991642504')
    print(calls_info)
    # https://zvonok.com/manager/cabapi_external/api/v1/phones/call/?campaign_id=2085175147&phone=+79991642504&public_key=a457c770b46296486b078f00f4ff444f
