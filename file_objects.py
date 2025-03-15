#  to open a file(not recommendedo)
# f = open('E:\\Codes\\Python_codes\\__pycache__\\movies.txt', 'r')
# # to get the file name
# print(f.name)
# #  to get the mode of opened file
# print(f.mode)
# f.close()
# recommended method is using context manager because it automatically closes file

with open('E:\\Codes\\Python_codes\\__pycache__\\movies.txt', 'r') as file:
    # print(file.name)
    # print(file.mode)
    # to read the contents of the file
    # print(file.read())
    # if the file is small above and other methods are used
    # print(file.readlines())
    #  this will print one line at a time
    # print(file.readline())
    # print(file.readline())
    # print(file.readline())
    # all the above methods will first save the cntents in ram and then run it
    # for large files this leads to memory issues, to avoid it we can iterate
    # for line in file:
    #     print(line, end= '')
    # we can even specify the no.of characters to be print
    # print(file.read(10))
    # print(file.read(10))
    # a funny way to read all the contecnts by using read
    # size_to_read = 3
    # file_contents = file.read(size_to_read)
    # while (len(file_contents) > 0):
    #     print(file_contents, end= '*')
    #     file_contents = file.read(size_to_read)
    # we can even tell in which position we are in the file
    # 
    #  we can even set our position to anywhere we like if we are reading by using read
    file_contents = file.read(3)
    print(file_contents)
    file.seek(0)
    file_contents = file.read(3)
    print(file_contents)