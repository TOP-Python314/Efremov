files_list = input().split('; ')
new_list = []
for i in range(len(files_list)):
    if files_list[i] not in new_list:
        new_list.append(files_list[i])
    else:
        
        first_dot_index = files_list[i].find('.')
        file_name = files_list[i][:first_dot_index]
        count_similar_names = 2
        
        while True:
            new_file_name = f'{file_name}_{count_similar_names}{files_list[i][first_dot_index:]}'
            if new_file_name in files_list:
                count_similar_names += 1
            else:
                count_similar_names = 2
                break
        
        new_list.append(new_file_name)
print('', *sorted(new_list), sep='\n') # '' для удобства

# 39.txt; 39.py; color.jpg; color_red.jpg; 39_2.py; main.com; abracadabra.magic; 39.py

    # 39.py
    # 39.txt
    # 39_2.py
    # 39_3.py
    # abracadabra.magic
    # color.jpg
    # color_red.jpg
    # main.com