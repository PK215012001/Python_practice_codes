# porgramme to play with csv files
import csv

# with open(f"E:\\Codes\\Python_codes\\__pycache__\\random_csv.csv", 'r') as f:
#     csv_reader = csv.reader(f)
#     with open('csv2.csv', 'w', newline= '') as temp:
#         csv_writer = csv.writer(temp, delimiter= '|')
#         csv_writer.writerows(csv_reader)

# with open('csv2.csv', 'r') as f:
#     read = csv.reader(f)
#     for line in read:
#         print(line)

#  we can use dict _reader and dict_writer for even more clarity
with open('E:\\Codes\\Python_codes\\__pycache__\\random_csv.csv', 'r') as f:
    dict_reader = csv.DictReader(f)
    with open('csv3.csv', 'w', newline= '') as temp:
        fieldname = ['Name', 'Age', 'City']
        dict_writer = csv.DictWriter(temp, delimiter= '|', fieldnames= fieldname)
        dict_writer.writeheader()
        dict_writer.writerows(dict_reader)