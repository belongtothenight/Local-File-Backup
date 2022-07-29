import shutil
from os import system, listdir
from os.path import isfile, join, isdir
from functools import wraps
from timeit import default_timer
from time import strftime, localtime
from datetime import date

# Startup
start = default_timer()
system('cls')
print("[LOG] Start executing lfb.py\n")

# Variables
src_1 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/src/ffc.pyw'
src_2 = './src/backup_test/src/'
src_3 = '.'
src_4 = 'c:/'
src_5 = 'd:/'
dst = './src/backup_test/dst/'
pattern = shutil.ignore_patterns('*.gitignore', '*.exe')

# copy single file
# status = shutil.copy2(src_1, dst)
# print("[LOG] " + str(status))

# copy everything inside the given directory
# tree = shutil.copytree(src_2, dst, ignore=pattern, copy_function=shutil.copy2, dirs_exist_ok=True) 
# print("[LOG] " + tree)

# print out the files in the directory (same layer)
# onlyfiles = [f for f in listdir(src_3) if isfile(join(src_3, f))]
# print("[LOG] " + onlyfiles)

# get all the element of the same layer
# print("[LOG] " + listdir(src_3))

# get all the folder in the directory (same layer)
# onlyfiles = [f for f in listdir(src_3) if not isfile(join(src_3, f))]
# onlyfiles = [f for f in listdir(src_3) if isdir(join(src_3, f))]
# print("[LOG] " + onlyfiles)

def process_directory(directory):
    '''
    Args:
        directory: (list) directory to be processed
    Returns:
        directory: (list) processed directory
    '''
    for element in directory:
        if '\\' in element:
            element = element.replace('\'', '\\\'')
        if '\\\\' in element:
            element = element.replace('\\\\', '\\')
    return directory

def list_all_files(path, file_directory, error_message):
    '''
    Args:
        path: (str) path to be processed
        file_directory: (list) empty list to be filled with file directories
        error_message: (list) empty list to be filled with error messages
    Returns:
        file_directory: (list) file directories
        error_message: (list) error messages
    '''
    try:
        for f in listdir(path):
            if isfile(join(path, f)):
                file_directory.append(join(path, f))
            elif isdir(join(path, f)):
                list_all_files(join(path, f), file_directory, error_message)# recursive call
            else:
                print("[LOG] Unknown file type: " + join(path, f))
    except Exception as e:
        error_message.append(str(e))
        print("[LOG] Error: " + str(e))
    return file_directory, error_message

fd = []
err = []
fd_1, err_1 = list_all_files(src_4, fd, err)
fd = [] # reset the list
err = [] # reset the list
fd_2, err_2 = list_all_files(src_5, fd, err)
fd = [] # reset the list
err = [] # reset the list
del fd[:], err[:] # this delete the list

# End
stop = default_timer()
print("[LOG] Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing lfb.py\n")

'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
'''