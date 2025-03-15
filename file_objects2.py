# if the opened file doesn't exists, then new file will be created
# otherwise exisiting fill will be overwritten
# with open('E:\\Codes\\Python_codes\\__pycache__\\test.txt', 'w') as file:
#     file.write(f'Test1\n')
#     file.write('kjsdhf')
#  a way to copy contents in one file to another
with open('E:\\Codes\\Python_codes\\__pycache__\\movies.txt', 'r') as rf:
    with open('E:\\Codes\\Python_codes\\__pycache__\\movies2.txt', 'w') as wf:
        for line in rf:
            wf.write(line)