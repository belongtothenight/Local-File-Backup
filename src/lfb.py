from concurrent.futures import process
from logging import root
from shutil import disk_usage, copy2, make_archive
from os import system, listdir, stat, walk
from os.path import isfile, join, isdir
from pathlib import Path
from timeit import default_timer
from time import strftime, localtime
from datetime import date, datetime, timezone
from sys import argv
from multiprocessing import Process

from numpy import append

# Startup
start = default_timer()
system('cls')
print("[LOG] Start executing {0}\n".format(Path(argv[0]).name))

# Variables
# parent_path = Path(__file__).parent.resolve() # get file path
parent_path = Path().parent.resolve() # get working directory path
src_1 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/src/ffc.pyw'
src_2 = './src/backup_test/src/'
src_3 = '.'
src_4 = 'c:/'
src_5 = 'd:/'
src_6 = 'e:/'
src_7 = 'f:/'
src_8 = './src/log/'
dst_2 = './src/backup_test/dst/'
log = []

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

# Store all src and dst file info into a list
fd, err, size, atime, mtime, ctime = create() # create empty lists
fd_src, err_src, size_src, atime_src, mtime_src, ctime_src = list_all_files(src_2, fd, err, size, atime, mtime, ctime)
fd, err, size, atime, mtime, ctime = create() # reset
fd_dst, err_dst, size_dst, atime_dst, mtime_dst, ctime_dst = list_all_files(dst_2, fd, err, size, atime, mtime, ctime)
fd, err, size, atime, mtime, ctime = create() # reset
tfs_src = sum_file_size(size_src)
tfs_dst = sum_file_size(size_dst)
tfs = tfs_src + tfs_dst
del fd[:], err[:], size[:], atime[:], mtime[:], ctime[:] # this delete the variables

# Gather disk usge info
total_src, used_src, free_src = disk_usage(src_2)
total_dst, used_dst, free_dst = disk_usage(dst_2)
total = total_src + total_dst
used = used_src + used_dst
free = free_src + free_dst


# Copy files
for i in range(len(fd_src)):
    try:
        # File with same name in dst
        j = fd_dst.index(join(dst_2, Path(fd_src[i]).name))
        # print("[LOG] Find file: " + fd_src[i])
        if size_src[i]==size_dst[j] and atime_src[i]==atime_dst[j] and mtime_src[i]==mtime_dst[j]:
            # File has the same metadata beside creation time
            print("[LOG] File is the same, skip " + fd_src[i])
            log.append("[LOG] File is the same, skip " + fd_src[i])
            continue
        else:
            # File has different metadata
            print("[LOG] File is different, copy " + fd_src[i])
            log.append("[LOG] File is different, copy " + fd_src[i])
            copy2(fd_src[i], dst_2)
    except Exception as e:
        # File is not found in dst
        print("[LOG] File is not found in dst, copy" + fd_src[i])
        log.append("[LOG] File is not found in dst, copy" + fd_src[i])
        copy2(fd_src[i], dst_2)
        continue

# Archive the folder
an = 'test' # name of the archive
ap = join(parent_path, dst_2.lstrip('./')) # archieve path
t_1 = default_timer()
make_archive(base_name=join(ap, an), format='gztar', root_dir=ap, base_dir=join(parent_path, src_2.lstrip('./')))
t_2 = default_timer()
log.append("[LOG] Archive {0}.tar.gz created. \t\tTakes {1} seconds.".format(an, t_2-t_1))
make_archive(base_name=join(ap, an), format='zip', root_dir=ap, base_dir=join(parent_path, src_2.lstrip('./')))
t_3 = default_timer()
log.append("[LOG] Archive {0}.zip created. \t\tTakes {1} seconds.".format(an, t_3-t_2))

# Gather and sort file name
files = [] # Filename in wrong order
buf = []
buf1 = []
fcnt = []
# Get all file name and generate new file number to avoid overwriting
for (dirpath, dirnames, filenames) in walk(join(parent_path, src_8.lstrip('./'))):
    files.extend(filenames)
    break
for i in range(len(files)):
    buf = files[i].split('_')
    buf = list(buf[-1])
    for j in range(len(buf)):
        try:
            buf1.append(int(buf[j]))
        except:
            continue
        buf1 = [str(k) for k in buf1]
        buf2 = ''.join(buf1)
        fcnt.append(buf2)
    buf1.clear()
fcnt = [int(i) for i in fcnt]
fcnt.sort()

# Write to log file
f = open(join(join(parent_path, src_8), 'log_{0}_{1}.txt'.format(str(date.today()), str(fcnt[-1]+1))), 'w', encoding='utf-8')
for element in log:
    f.write(str(date.today()) + " " + strftime("%H:%M:%S", localtime()) + " " + element + "\n")
f.close()

# End
stop = default_timer()
print("[LOG] Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing {0}\n".format(Path(argv[0]).name))

'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
https://docs.python.org/3/library/stat.html
'''