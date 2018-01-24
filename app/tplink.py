import requests
import config
import utils
import time


def get_token():
    """Get token from tplink."""

    tplink_cfg = config.get()['tplink']

    body = {
        'method': 'login',
        'params': {
            'appType': 'Kasa_Android',
            'cloudUserName': tplink_cfg['cloud_user_name'],
            'cloudPassword': tplink_cfg['cloud_password'],
            'terminalUUID': tplink_cfg['terminal_UUID']
        }
    }

    print 'Getting token'
    response = requests.post(tplink_cfg['url'], json=body)
    json_response = response.json()
    print 'Token received'
    return json_response['result']['token']


def get_device_id(name):
    """Get device ID based on name."""

    tplink_cfg = config.get()['tplink']
    url = tplink_cfg['url'] + '?token=' + get_token()

    print 'Getting device list'
    response = requests.post(url, json={'method': 'getDeviceList'})
    response_json = response.json()
    print 'Device list received'
    device_id = None

    for device in response_json['result']['deviceList']:
        if name == device['alias']:
            return device['deviceId']

    return device_id


def switch(rig_name, state):
    """Switch on(1) / off(0) rig."""

    if state == 1:
        mode = 'on'
    else:
        mode = 'off'

    tplink_cfg = config.get()['tplink']

    body = {
        'method': 'passthrough',
        'params': {
            'deviceId': get_device_id(utils.get_tplink_name(rig_name)),
            'requestData': '{"system":{"set_relay_state":{"state":' + str(state) + '}}}'
        }
    }

    url = tplink_cfg['url'] + '?token=' + get_token()
    print 'Switching ' + mode + ' rig ' + rig_name + ' [' + utils.get_tplink_name(rig_name) + ']'
    response = requests.post(url, json=body)
    response_json = response.json()
    if response_json['error_code'] == 0:
        print 'Switched ' + mode
    else:
        print 'Cannot switch ' + mode


def reset(rig_name):
    switch(rig_name, 0)
    time.sleep(config.get()['reset_interval_seconds'])
    switch(rig_name, 1)
