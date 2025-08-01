import os
import zipfile

# Пути
tmp_dir = r'C:\Homework7\tmp'
zip_path = r'C:\Homework7\test.zip'

# Файлы для добавления
add_file = os.path.join(tmp_dir, 'csv1.csv')
add_file2 = os.path.join(tmp_dir, 'pdfka.pdf')
add_file3 = os.path.join(tmp_dir, 'summy.xlsx')

# Проверка, что папка с файлами существует
if not os.path.isdir(tmp_dir):
    raise FileNotFoundError(f"Папка не найдена: {tmp_dir}")

# Проверка, что архив существует
if not os.path.isfile(zip_path):
    raise FileNotFoundError(f"Архив не найден: {zip_path}")

# Проверка, что файлы для добавления существуют
for f in [add_file, add_file2, add_file3]:
    if not os.path.isfile(f):
        raise FileNotFoundError(f"Файл для добавления не найден: {f}")

# Добавление файлов в архив
with zipfile.ZipFile(zip_path, mode='a', compression=zipfile.ZIP_DEFLATED) as zf:
    zf.write(add_file, arcname=os.path.basename(add_file))
    zf.write(add_file2, arcname=os.path.basename(add_file2))
    zf.write(add_file3, arcname=os.path.basename(add_file3))

print(" Файлы добавлены в архив:", zip_path)
 # Список файлов которые у нас добаваляет скрипт
with zipfile.ZipFile('test.zip', mode='a') as zf:
    for file in zf.namelist():
        print(file)