import yaml

config = False

def get():
    global config
    if config is False:
        print 'Loading configuration'
        with open('./config.yml', 'r') as ymlfile:
            config = yaml.load(ymlfile)
    return config
