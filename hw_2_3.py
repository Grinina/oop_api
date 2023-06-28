import os
current = os.getcwd()
from pprint import pprint
folder_name_1 = 'py-homework-basic-files'
folder_name_2 = '2.4.files'
folder_name_3 = 'sorted'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
full_path_1 = os.path.join(current, folder_name_1, folder_name_2, folder_name_3, file_name_1)
full_path_2 = os.path.join(current, folder_name_1, folder_name_2, folder_name_3, file_name_2)
full_path_3 = os.path.join(current, folder_name_1, folder_name_2, folder_name_3, file_name_3)
target_file_name = '4.txt'
full_path_target = os.path.join(current, folder_name_1, folder_name_2, folder_name_3, target_file_name)
count = []
with open(full_path_target, 'wt') as target_file:

    with open(full_path_1, 'rt', encoding='utf-8') as file:
        file_book_1 = {}
        file_text = []
        file_book_1['file_name'] = file_name_1
        for n, line in enumerate(file, 1):

            line = line.rstrip('\n')
            file_text.append(line)
            file_book_1 = {file_name_1 : {'line_count': n, 'file_text': file_text}}
        count.append(n)
    with open(full_path_2, 'rt', encoding='utf-8') as file:
        file_book_2 = {}
        file_text = []
        file_book_2['file_name'] = file_name_2
        for n, line in enumerate(file, 1):
            line = line.rstrip('\n')
            file_text.append(line)
            file_book_2 = {file_name_2 : {'line_count': n, 'file_text': file_text}}
        count.append(n)
    with open(full_path_3, 'rt', encoding='utf-8') as file:
        file_book_3 = {}
        file_text = []
        file_book_3['file_name'] = file_name_3
        for n, line in enumerate(file, 1):
            line = line.rstrip('\n')
            file_text.append(line)
            file_book_3 = {file_name_3 : {'line_count': n, 'file_text': file_text}}
        count.append(n)
    result = []
    list_file_information = [file_book_1, file_book_2,file_book_3]
    for i in sorted(count):
        for x in list_file_information:
            for k, v in x.items():
                if i == v['line_count']:
                   text = v['file_text']
                   z = "\n".join(text)
                   res= f"{k}\n{i}\n{z}\n"
                   result.append(res)
    target_file.writelines(result)




# target_file_name = '4.txt'
# full_path_target = os.path.join(current, folder_name_1, folder_name_2, folder_name_3, target_file_name)
# with open(full_path_target, 'wt') as file:
#     file.writelines(str(''.join(file_book_1['file_text'])))



