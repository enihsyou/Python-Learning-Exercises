# import subprocess
#
# p = subprocess.Popen('D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise_scale --scale_ratio 1.6 --noise_level 2', shell = True, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
# for line in p.stdout.readlines():
#     print(line)



# a = b'\x95\xcf\x8a\xb7\x82\xc9\x90\xac\x8c\xf7\x82\xb5\x82\xdc\x82\xb5\x82\xbd\r\n'
# print(a.decode('gbk'))
# print(a.decode('shift_jis'))

import os

# b = os.popen('D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise --noise_level 2').readlines()
# b = ['曄姺偵惉岟偟傑偟偨\n']
# print(bytes(b[0].encode('gbk')).decode('shift-jis'))

# b = r'D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe'
# input_path = r'-i D:\test\001.jpg'
# mode = r'-m noise'
# noise_level = r'--noise_level 2'
# c = [b, input_path, mode, noise_level]
#
# print(" ".join(c))
# 'D:\Download\waifu2x-caffe\waifu2x-caffe\waifu2x-caffe-cui.exe -i D:\test\001.jpg -m noise --noise_level 2'


import subprocess, shlex

command_line = input()
args = shlex.split(command_line)
print(args)
p = subprocess.Popen(args)
print(p)
