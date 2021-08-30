#! python3
# backup.py


import zipfile
import os

print("输入需要备份的文件夹地址：",end=' ')
file = input()

def backup(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + 'V1.' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print('备份包创建中 %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('正在添加文件 %s...' % (foldername))
        backupZip.write(foldername)

        for filename in filenames:
            if filename.startswith(os.path.basename(folder) + '_') and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


backup(file)
