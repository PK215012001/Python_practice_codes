import os
import datetime
# to get the current working directory
# print(os.getcwd())
# to change the diectory
# os.chdir('D:')
# print(os.getcwd())
# to get the files in the directory
# print(os.listdir())
# os.chdir('D:\\Movies')
# print(os.listdir())
# to create new files
# os.makedirs('Pavan\\movie_data')
# print(os.listdir())
# os.chdir('Pavan')
# print(os.getcwd())
# print(os.listdir())
# to remove files
# print(os.getcwd())
# os.chdir('D:')
# print(os.listdir())
# os.rmdir('text_data')
# print(os.listdir())
# os.chdir('text_data')
# print(os.listdir())
# os.rmdir('movies_data')
# print(os.listdir())
# os.chdir('D:')
# print(os.listdir())
# os.rmdir('text_data')
# print(os.listdir())
# to rename a file
# os.rename('basic.py', 'demo.py')
# print(os.listdir())
# to get the stats of a file
# print(os.stat('demo.py'))
# mod_time = os.stat('demo.py').st_mtime
# print(mod_time)
# #  to get the timestamp in human readable form
# print(datetime.datetime.fromtimestamp(mod_time))
#  to traverse all the way inside a directory
# for dirpath, dirname, filenames in os.walk('D:\\'):
#     print('dirpath: ',dirpath)
#     print('dirname: ', dirname)
#     print('files: ', filenames)
#     print()
# print(os.environ.get('HOME'))
# to know whether a path is file or dir
print(os.path.isdir('D:\\'))