import alive_detector
import tplink


print 'Application started...'

rigs = alive_detector.miners_alive()

for rig in rigs:
    if rig['alive'] is False:
        print 'Rig ' + rig['name'] + ' is down. Starting reset...'
        tplink.reset(rig['name'])

print 'Application finished'
