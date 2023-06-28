import requests

TOKEN = '6058058880:AAFnv-Fo1BWFyvk9kY-LPS-JLqYnl_W9M4Q'


# kick.kick_from_groups()

emails = ['webstyle2011@tut.by']
result_orders = {}
from_ind = 0
to_ind = 100
while True:
    params = {'type': 'bot_api_get_update_balance_by_email', "token": "sadf432523fsdaf45267erh23"}
    check_email = emails[from_ind: to_ind]
    if len(check_email) == 0:
        break
    from_ind += 100
    to_ind += 100
    for idx, email in enumerate(check_email):
        params[f'email[{idx}]'] = email

    res = requests.get("https://pigment-shop.com/local/cron/scripts/bot_api.php", params)
    result_orders.update(res.json())
print(result_orders)
print(len(result_orders))
