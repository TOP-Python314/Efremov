import utils
import os

def ask_for_file() -> str:
    flag = True
    file_path = input('путь: ')
    while flag == True:
        a = file_path.rfind('\\')
        file_folder = file_path[:a]
        file = file_path[a+1:]
        files_list = os.listdir(file_folder)
        if file in files_list:
            flag = False
            new_file = utils.load_file(file_path)
            import conf
            return conf
        else:
            print('! По указанному пути отсутствует необходимый файл !')
            file_path = input('путь: ')

# >>> config_module = ask_for_file()
# путь: D:\TOP\Python\Выполнено\Efremov\2023.12.28\conf.py
# ! По указанному пути отсутствует необходимый файл !
# путь: D:\TOP\Python\Выполнено\Efremov\2023.12.28\data\conf.py
# >>>
# >>> config_module.defaults
# {'parameter1': 'value1', 'parameter2': 'value2', 'parameter3': 'value3', 'parameter4': 'value4'}
