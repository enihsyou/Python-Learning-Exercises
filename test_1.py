# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('www.pythonlearn.com', 80))
# mysock.send(b'GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n')

# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data)

# mysock.close()
import urllib.request as ur
fhand = ur.urlopen('http://www.pythonlearn.com/code/intro-short.txt')
for key, value in fhand.getheaders():
    print(key, value)
    