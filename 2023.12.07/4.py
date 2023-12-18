errors_list = []

while True:
    error_text = input()
    if error_text != '':
        errors_list.append(error_text.split()[::-1])
    else:
        break

error_name = input()
if error_name in dict(errors_list):
    print(dict(errors_list)[error_name])
else:
    print('! value error !')

# Ввод 1:
    # 276 ER_DEEPFAKE_MISSMATCH_FACE
    # 277 ER_DEEPFAKE_FACE_MATHES
    # 344 ER_CANT_COPY_NAME
    # 346 ER_CANT_COPY_ADDRESS

    # ER_CANT_COPY_NAME
    
    # 344
    
# Ввод 2:    
    # 4056 ER_INCORRECT_LOG
    # 4057 ER_INCORRECT_PASSWORD
    # 4348 ER_DROP_PC
    # 4444 ER_CANT_INVENT_ERROR

    # ER_FATALITY_MK
    
    # ! value error !