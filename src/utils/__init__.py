from configparser import ConfigParser
cf = ConfigParser.ConfigParser()
cf.read("src/config.conf")
secs = cf.sections()
print('sections:', secs)

opts = cf.options("db")
print('options:', opts)

kvs = cf.items("db")
print('db:', kvs)