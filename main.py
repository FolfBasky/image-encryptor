def img_to_txt(file: str) -> list:
    'return text of the pucture'
    with open(file, 'rb') as f:
        r = f.read()
        print(r)
    return list(r)

f_key = 44
def decriptor(img_txt: list, filename = 'file.jpg'):
    'make new dectiptor file'
    img_txt_copy = img_txt.copy()  # Создаем копию списка
    for x in range(50, len(img_txt_copy)):
        img_txt_copy[x] ^= f_key  # Применяем операцию XOR
    with open(filename, 'wb+') as f:
        f.write(bytes(img_txt_copy))

def encryptor(img_txt: list, filename = 'file1.jpg'):
    'encrypted a file'
    img_txt_copy = img_txt.copy()  # Создаем копию списка
    for x in range(50, len(img_txt_copy)):
        img_txt_copy[x] ^= f_key  # Применяем операцию XOR
    with open(filename, 'wb+') as f:
        f.write(bytes(img_txt_copy))

#img_to_txt('cat.jpg')
print(decriptor(img_to_txt('cat.jpg')))
print(encryptor(img_to_txt('file.jpg')))