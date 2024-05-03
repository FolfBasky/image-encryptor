import os
from time import sleep
import random
#import string

def img_to_txt(file: str) -> list:
    'return text of the pucture'
    with open(file, 'rb') as f:
        r = f.read()
    return list(r)

f_key = random.randint(22,99)
def decriptor(img_txt: list, filename:str = 'file', exp:str = 'jpg'):
    'make new dectiptor file'
    img_txt_copy = img_txt.copy()  # Создаем копию списка
    for x in range(50, len(img_txt_copy)):
        img_txt_copy[x] ^= f_key  # Применяем операцию XOR
    with open('dec/'+'.'.join([filename,exp]), 'wb+') as f:
        f.write(bytes(img_txt_copy))

def encryptor(img_txt: list, filename:str = 'file1', exp:str = 'jpg'):
    'encrypted a file'
    img_txt_copy = img_txt.copy()  # Создаем копию списка
    for x in range(50, len(img_txt_copy)):
        img_txt_copy[x] ^= f_key  # Применяем операцию XOR
    with open('enc/'+'.'.join([filename,exp]), 'wb+') as f:
        f.write(bytes(img_txt_copy))

def get_new_files(exp:str = 'jpg'):
    'check new files in dir'
    new_files = [i for i in [x[2] for x in os.walk('files')][0]]
    return new_files

def get_old_files(exp:str = 'jpg'):
    'check old files in dir'
    old_files = [i for i in [x[2] for x in os.walk('enc')][0]]
    return old_files

def check_new_files():
    'return True if have new files'
    return len([x.split('.') for x in get_new_files()]) > len([x.split('.') for x in get_old_files()])

def get_unique_files():
    return list(set(get_new_files())-set(get_old_files()))

while True:
    sleep(0.5)
    if check_new_files():
        res = get_unique_files()
        for el in res:
            name, exp = el.split('.')
            name_new = name
            #k = 45-len(name) if len(name) <= 45 else 0
            #name_new = name + ''.join(random.choices(''.join(string.ascii_lowercase), k = k))
            decriptor(img_to_txt('files/'+name+'.'+exp), name_new, exp)
            encryptor(img_to_txt('dec/'+name_new+'.'+exp), name_new, exp)
