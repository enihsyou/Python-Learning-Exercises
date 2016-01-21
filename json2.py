import json
import urllib.request as ur

url = input('Enter: ')
# if len(url) < 1: url = 'http://python-data.dr-chuck.net/comments_42.json'
if len(url) < 1: url = 'http://python-data.dr-chuck.net/comments_202175.json'
ha = ur.urlopen(url)
data = ha.read().decode('utf-8')
info = json.loads(data)
print('Numbers:', len(data))
sum = 0
print(json.dumps(info))
for v in info:
    if v == "note": continue
    for item in info[v]:
        print('Name', item['name'], 'Count', item['count'])
        sum += item['count']

print(sum)
