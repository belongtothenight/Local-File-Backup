import shutil
import os
import sys

os.system('cls')

src = './backup_test/1/ffc.pyw'
dst = './backup_test/2/'

status = shutil.copy2(src, dst)
print(status)

'''
https://github.com/belongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
'''