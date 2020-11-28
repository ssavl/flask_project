import requests
from config import api_key, URL
from requests.exceptions import RequestException, Timeout


def get_weather(city_name):
    params = {
        'key': api_key,
        'q': city_name,
        'format': 'json',
        'date': 'today'
    }
    try:
        req = requests.get(URL, params=params)
        req.raise_for_status()
        result = req.json()
    except (RequestException, Timeout):
        return 'Проблемы на сервере погоды'
    if result:
        if 'data' in result:
            if 'current_condition' in result['data']:
                try:
                    time_now = result['data']['current_condition'][0]['observation_time']
                    temp = result['data']['current_condition'][0]['temp_C']
                    temp_real = result['data']['current_condition'][0]['FeelsLikeC']
                    return f'Сейчас {time_now}, температура в {city_name} = {temp}, но ощущается как {temp_real}'
                except Exception:
                    print('Возинкли проблемы при составлении запроса')
    return 'Возникли проблемы'
