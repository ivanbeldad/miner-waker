import requests
import config

def get_token():
    """Get token from tplink."""

    tplink_cfg = config.get()

    credentials = {
        'method': 'login',
        'params': {
            'appType': 'Kasa_Android',
            'cloudUserName': tplink_cfg['cloud_user_name'],
            'cloudPassword': tplink_cfg['cloud_password'],
            'terminalUUID': tplink_cfg['terminal_UUID']
        }
    }

    print 'Getting token'
    response = requests.post(tplink_cfg['url'], json=credentials)
    json_response = response.json()
    print 'Token received'
    return json_response['result']['token']
