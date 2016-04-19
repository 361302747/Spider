import configparser
cf=configparser.ConfigParser()
print("use ConfigParser() read")

cf.read('../config.conf')

sections = cf.sections()
print('sections',sections)
options = cf.options("db")
print(options)
print(cf.get('db','user'))
print(cf.items("db"))
# print ("use ConfigParser() write")
# cf.set("portal", "url2", "%(host)s:%(port)s")
# print(cf.get("portal", "url2"))