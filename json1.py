import json
import urllib.request as ur

# handle = ur.urlopen("http://api.hitokoto.us/rand?cat=a&charset=utf-8")
# a1 = handle.read().decode('utf-8')
# info = json.loads(a1)
# print('的九分裤的境况')
# print(a1)
# print(info)
# print(json.dumps(info, indent = 4, ensure_ascii = False))
print(json.loads('[ {"Glenn":1}, "Sally", "Jen" ]'))