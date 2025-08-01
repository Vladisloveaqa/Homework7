# В этом скрипте я создаю архив
import os.path
import zipfile
import zipfile as zip
path = '/Homework7/tmp'
file_dir = os.listdir(path)

with zipfile.ZipFile('test.zip', mode='w', \
                     compression=zipfile.ZIP_DEFLATED) as zf:
    for file in file_dir:
        add_file = os.path.join(path, file)
        zf.write(add_file)
