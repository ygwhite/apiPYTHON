import requests
import json

class MyAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = 'https://pigment-shop.com/local/cron/scripts/bot_api.php'

    def get_orders_by_email(self, emails):
        params = {
            'type': 'bot_api_get_orders_by_email',
            'token': self.token
        }
        for idx, email in enumerate(emails):
            params[f'email[{idx}]'] = email

        response = requests.get(self.base_url, params=params)
        try:
            data = json.loads(response.text)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return {}

    def get_balance_by_email(self, emails):
        params = {
            'type': 'bot_api_get_balance_by_email',
            'token': self.token
        }
        for idx, email in enumerate(emails):
            params[f'email[{idx}]'] = email

        response = requests.get(self.base_url, params=params)
        try:
            data = json.loads(response.text)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return {}

    def update_balance_by_email(self, email, price):
        params = {
            'type': 'bot_api_get_update_balance_by_email',
            'token': self.token,
            'price': price,
            'email[0]': email
        }

        response = requests.get(self.base_url, params=params)
        try:
            data = json.loads(response.text)
            return data
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON response: {e}")
            return {}

# Использование класса
TOKEN = 'sadf432523fsdaf45267erh23'
api = MyAPI(TOKEN)

emails = ['kseniya.pylina@mail.ru', 'talbetka2111777@mail.ru']
result_orders = api.get_orders_by_email(emails)
result_balance = api.get_balance_by_email(emails)
result_update_balance = api.update_balance_by_email('webstyle2011@tut.by', -40)

print(result_orders)
print(len(result_orders))

print(result_balance)
print(len(result_balance))

print(result_update_balance)
print(len(result_update_balance))
