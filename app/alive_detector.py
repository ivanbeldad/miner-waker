import requests
import config


def miners_alive():
    """Check if miners are alive."""

    response = requests.get(config.get()['ethos']['api_url'])
    rigs = response.json()['rigs']

    alive_rigs = [{
        'name': rig,
        'alive': rigs[rig]['condition'] == 'mining'
    } for rig in rigs]

    return alive_rigs
