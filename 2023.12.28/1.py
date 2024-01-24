from pathlib import Path
from sys import path
import os

def list_files(absolut_path: str) -> tuple:
    
    os.chdir(absolut_path)
    p = list(Path('.').glob('*.*'))
    list_path = [str(x) for x in p]
    return tuple(list_path)
    
# D:\TOP\Python\Выполнено\Efremov\2023.12.28>tree /f
# Структура папок тома Data
# Серийный номер тома: 8228-BFCB
# D:.
# │   # HW 2023.12.28.txt
# │   1.py
# │   2.py
# │   3.py
# │   4.py
# │   5.py
# │   6.py
# │   conf.py
# │   python
# │   tree
# │   utils.py
# │
# ├───data
# │   │   7MD9i.chm
# │   │   conf.py
# │   │   E3ln1.txt
# │   │   F1jws.jpg
# │   │   function_calls.log
# │   │   le1UO.txt
# │   │   q40Kv.docx
# │   │   questions.quiz
# │   │   r62Bf.txt
# │   │   vars.py
# │   │   xcD1a.zip
# │   │
# │   ├───c14KE
# │   │       5vsIh.dat
# │   │       P2a91.dat
# │   │
# │   ├───mXbd9
# │   │       RoBjg.pt
# │   │       z03EN.pt
# │   │
# │   └───__pycache__
# │           conf.cpython-312.pyc
# │
# └───__pycache__
        # conf.cpython-312.pyc
        # utils.cpython-312.pyc
# D:\TOP\Python\Выполнено\Efremov\2023.12.28>python -i 1.py
# >>> list_files(r'D:\TOP\Python\Выполнено\Efremov\2023.12.28\data')
# ('7MD9i.chm', 'conf.py', 'E3ln1.txt', 'F1jws.jpg', 'function_calls.log', 'le1UO.txt', 'q40Kv.docx', 'questions.quiz', 'r62Bf.txt', 'vars.py', 'xcD1a.zip')        
        