import shutil
import os
from sys import path
from pathlib import Path

def important_message(text_message: str) -> str:    
    header_frame_w, header_frame_h = shutil.get_terminal_size()
    text_message = text_message + ' '
    text_out = ''
    while text_message != ' ':
        s = text_message[:header_frame_w-7].rfind(' ')
        text_out += f' #  {text_message[:s].center(header_frame_w-7)}  #'
        text_message = text_message[s:]
        
    return (f'#{(header_frame_w-3)*"="}#'
           f' #{"".center(header_frame_w-3)}#'        
           f'{text_out}'
           f' #{"".center(header_frame_w-3)}#'
           f' #{(header_frame_w-3)*"="}#')          


def load_file(file_path: str):
    shutil.copy2(file_path, Path(path[0]))
    new_file_path = Path(path[0]) / file_path.split('\\')[-1]
    return new_file_path
    
def correct_answer(answer: str) -> str:
        if '+' in answer:
            return True
        else:
            return False
            
    