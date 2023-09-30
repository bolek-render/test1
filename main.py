import os
import shutil
import math

path = os.getcwd()
disk = shutil.disk_usage(path)


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])


print()
print(f'current path : {path}')
print()
print('DISK USAGE STATS :')
print(f'total : {convert_size(disk.total)}')
print(f'free : {convert_size(disk.free)}')
print(f'used : {convert_size(disk.used)}')
print()

if os.path.isfile('file.txt'):
    file_read = open('file.txt', 'rt')
    print(f'file read : {file_read.read()}')
    print()

text = 'Input text to file : '
print()

with open('file.txt', 'wt') as file:
    file.write(text)

