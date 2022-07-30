from shutil import disk_usage, ignore_patterns, copy2, copytree
from os import system, listdir, stat
from os.path import isfile, join, isdir
from timeit import default_timer
from time import strftime, localtime
from datetime import date, datetime, timezone

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

# copy single file
# status = copy2(src_1, dst)
# print("[LOG] " + str(status))

# copy everything inside the given directory
# pattern = ignore_patterns('*.gitignore', '*.exe')
# tree = copytree(src_2, dst, ignore=pattern, copy_function=copy2, dirs_exist_ok=True) 
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

def list_all_files(path, file_directory, error_message, file_size, atime, mtime, ctime):
    '''
    Args:
        path: (str) path to be processed
        file_directory: (list) empty list to be filled with file directories
        error_message: (list) empty list to be filled with error messages
        file_size: (list) empty list to be filled with file size
        atime: (list) empty list to be filled with access time
        mtime: (list) empty list to be filled with modification time
        ctime: (list) empty list to be filled with creation time
    Returns:
        file_directory: (list) file directories
        error_message: (list) error messages
        file_size: (list) file size
        atime: (list) access time
        mtime: (list) modification time
        ctime: (list) creation time
    '''
    try:
        for f in listdir(path):
            if isfile(join(path, f)):
                file_directory.append(join(path, f))
                file_size.append(stat(join(path, f)).st_size)
                atime.append(datetime.fromtimestamp(int(stat(join(path, f)).st_atime)))
                mtime.append(datetime.fromtimestamp(int(stat(join(path, f)).st_mtime)))
                ctime.append(datetime.fromtimestamp(int(stat(join(path, f)).st_ctime)))
            elif isdir(join(path, f)):
                list_all_files(join(path, f), file_directory, error_message, file_size, atime, mtime, ctime)# recursive call
            else:
                print("[LOG] Unknown file type: " + join(path, f))
    except Exception as e:
        error_message.append(str(e))
        print("[LOG] Error: " + str(e))
    return file_directory, error_message, file_size, atime, mtime, ctime

def sum_file_size(size_list):
    '''
    Args:
        size_list: (list) file size list
    Returns:
        total_size: (int) total file size
    '''
    total_size = 0
    for size in size_list:
        total_size += size
    return total_size

def create():
    '''
    Args:
        None
    Returns:
        fd: (list) empty file directory
        em: (list) empty error message
        ts: (list) empty total file size
    '''
    a = []
    b = []
    c = []
    d = []
    e = []
    f = []
    return a, b, c, d, e, f

fd, err, size, atime, mtime, ctime = create() # create empty lists
fd_1, err_1, size_1, atime_1, mtime_1, ctime_1 = list_all_files(src_4, fd, err, size, atime, mtime, ctime)
fd, err, size, atime, mtime, ctime = create() # reset
fd_2, err_2, size_2, atime_2, mtime_2, ctime_2 = list_all_files(src_5, fd, err, size, atime, mtime, ctime)
fd, err, size, atime, mtime, ctime = create() # reset
tfs_1 = sum_file_size(size_1)
tfs_2 = sum_file_size(size_2)
tfs = tfs_1 + tfs_2
del fd[:], err[:], size[:], atime[:], mtime[:], ctime[:] # this delete the variables

total_1, used_1, free_1 = disk_usage(src_4)
total_2, used_2, free_2 = disk_usage(src_5)
total = total_1 + total_2
used = used_1 + used_2
free = free_1 + free_2

# End
stop = default_timer()
print("[LOG] Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing load_disk_to_mem.py\n")

'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
https://docs.python.org/3/library/stat.html
'''