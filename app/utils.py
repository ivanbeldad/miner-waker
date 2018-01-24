import config


def get_tplink_name(rig_name):
    """Get tplink name device based on rig name."""

    miners = config.get()['miners']

    for mine in miners:
        if mine['rig_name'] == rig_name:
            return mine['tplink_name']
    return None


def get_rig_name(tplink_name):
    """Get rig name device based on tplink name."""

    miners = config.get()['miners']

    for mine in miners:
        if mine['tplink_name'] == tplink_name:
            return mine['rig_name']
    return None
