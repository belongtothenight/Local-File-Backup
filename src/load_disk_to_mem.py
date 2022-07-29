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
print("[LOG] Start executing load_disk_to_mem.py\n")

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
print("[LOG] End executing load_disk_to_mem.py\n")
# del variable # clear variable

# Write log
f = open('./src/log/all_accessible_files.txt', 'w', encoding='utf-8')
f.write("This is a list of all accessible files currently in my laptop.\n")
f.write("Executed at: " + str(date.today()) + " " + strftime("%H:%M:%S", localtime()) + "\n")
f.write("Runtime: " + str(stop - start) + " seconds\n")
f.write("Total number of accessible files in " + src_4 + " : " + str(len(fd_1)) + "\n")
f.write("Total number of accessible files in " + src_5 + " : " + str(len(fd_2)) + "\n")
f.write("Total number of inaccessible files in " + src_4 + " : " + str(len(err_1)) + "\n")
f.write("Total number of inaccessible files in " + src_5 + " : " + str(len(err_2)) + "\n")
f.write("Total number of accessible files: " + str(len(fd_1) + len(fd_2)) + "\n")
f.write("Total number of unaccessible files: " + str(len(err_1) + len(err_2)) + "\n")
f.write("\n\n")
f.write("All accessible files in " + src_4 + ":\n\n")
for element in fd_1:
    f.write(element + "\n")
f.write("\n\n")
f.write("All accessible files in " + src_5 + ":\n\n")
for element in fd_2:
    f.write(element + "\n")
f.write("\n\n")
f.write("All unaccessible files in " + src_4 + ":\n\n")
for element in err_1:
    f.write(element + "\n")
f.write("\n\n")
f.write("All unaccessible files in " + src_5 + ":\n\n")
for element in err_2:
    f.write(element + "\n")
f.close()

'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
'''