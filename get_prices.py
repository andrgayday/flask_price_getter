import requests
from environs import Env


env = Env()
env.read_env()

yandex_functions_url = "https://functions.yandexcloud.net/"
yandex_function_id = env("SERVERLESS_FUNCTION_ID")
url = yandex_functions_url + yandex_function_id


def get_prices_from_binance(params):
    try:
        # Выполняем GET-запрос
        response = requests.get(url, params=params)
        
        # Проверяем статус-код
        if response.status_code == 200:
            # Получаем JSON ответ
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None