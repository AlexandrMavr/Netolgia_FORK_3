import os

BASE_PATH = os.getcwd()
log_dir ='logs'
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'

list_file = [file_name_1, file_name_2, file_name_3]

def file_worker(file_name, mode, encoding):
    with open(file_name, mode, encoding=encoding) as file:
        line = 0
        for i in file:
            line += 1
    return line

file_book = {}

for i in list_file:
    file_book[i] = 0
    file_book[i] += int(file_worker(os.path.join(BASE_PATH, log_dir, i), "r", "utf-8"))


sorted_tuple = sorted(file_book.items(), key=lambda x: x[1])
file_book_sorted = dict(sorted_tuple)


def sum_file_and_info():
    with open('sum_file.txt', 'w') as outfile:
        count = 0
        for file_name in file_book_sorted:
            count += 1
            print(file_name)
            print(count)
            with open(os.path.join(BASE_PATH, log_dir, file_name)) as infile:
                count_line = 0
                for line in infile:
                    count_line += 1
                    outfile.write(line)
                    print(f"Строка номер {count_line} файла номер {count}")


sum_file_and_info()


