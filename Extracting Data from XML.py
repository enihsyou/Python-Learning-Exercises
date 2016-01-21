# import urllib.request as ur
import xml.etree.ElementTree as ET

fhand = open('comments_202171.xml')
# fhand = open('comments_42.xml')
files = fhand.read()

tree = ET.fromstring(files)
sums = 0
results = tree.findall('.//count')
for item in results:
    sums = sums + int(item.text)
print(sums)
