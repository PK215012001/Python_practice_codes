import os
from datetime import datetime
print(os.getcwd())
os.chdir('D:\\')
print(os.getcwd())
print(os.listdir())

#  to rename a file
# 

#  to check the contents of a file
print(os.stat('movie_list'))

timestamp = os.stat('movie_list').st_mtime
print(datetime.fromtimestamp(timestamp))