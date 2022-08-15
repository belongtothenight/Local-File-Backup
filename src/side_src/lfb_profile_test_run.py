from logging import root
from os import system
from os.path import basename, dirname
from pathlib import Path
from timeit import default_timer
from sys import argv
from lfb_lib import archive_single_file, get_file_info, get_folder_info, copy_file, archive_single_file, archive_folder, unpack_file, export_log

# Function


def multi_folder_copy(src, dst, size_src, size_dst, filecount_src, filecount_dst):
    file_info = get_file_info(src, dst)
    size_src.append(file_info[12])
    size_dst.append(file_info[13])
    filecount_src.append(len(file_info[0]))
    filecount_dst.append(len(file_info[6]))
    del file_info[:]
    return size_src, size_dst, filecount_src, filecount_dst


# Variables
log_path = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/log/'
src_a = 'D:/Computer File/'
src_b = 'D:/Note_Database/'
dst_a = 'E:/Computer File/'
dst_b = 'F:/Computer File/'
dst_c = 'F:/N_D BackUp/Partial Copy of ND 20220805/'
dst_d = 'E:/N_D BackUp/Partial Copy of ND 20220805/'
dst_e = 'F:/Note_Database/'
profile = [
    ['CF Backup My Passport', src_a, dst_b],
    ['CF Backup Transend', src_a, dst_a],
    ['ND Backup My Passport', src_b, dst_c],
    ['ND Backup Transend', src_b, dst_d],
    ['ND Full Backup My Passport', src_b, dst_e]
]

# Startup
start = default_timer()
system('cls')
print("[LOG] Start executing {0}\n".format(Path(argv[0]).name))
log = []
size_src = []
size_dst = []
filecount_src = []
filecount_dst = []

# Main
'''CF Backup My Passport'''
size_src, size_dst, filecount_src, filecount_dst = multi_folder_copy(
    profile[0][1], profile[0][2], size_src, size_dst, filecount_src, filecount_dst)
'''CF Backup Transend'''
size_src, size_dst, filecount_src, filecount_dst = multi_folder_copy(
    profile[1][1], profile[1][2], size_src, size_dst, filecount_src, filecount_dst)
'''ND Backup My Passport'''
size_src, size_dst, filecount_src, filecount_dst = multi_folder_copy(
    profile[2][1], profile[2][2], size_src, size_dst, filecount_src, filecount_dst)
'''ND Backup Transend'''
size_src, size_dst, filecount_src, filecount_dst = multi_folder_copy(
    profile[3][1], profile[3][2], size_src, size_dst, filecount_src, filecount_dst)
'''ND Full Backup My Passport'''
size_src, size_dst, filecount_src, filecount_dst = multi_folder_copy(
    profile[4][1], profile[4][2], size_src, size_dst, filecount_src, filecount_dst)

# Write Test Results to Log
log.append('Test Results:')
for i in range(len(profile)):
    log.append('\n')
    log.append('Profile: {0}'.format(profile[i][0]))
    log.append('Source:\t\t\t\t\t\t{0}'.format(profile[i][1]))
    log.append('Destination:\t\t\t\t{0}'.format(profile[i][2]))
    log.append('Source Size(GB):\t\t{:>12}'.format(
        str(size_src[i]//1024//1024//1024)))
    log.append('Destination Size(GB):\t{:>12}'.format(
        str(size_dst[i]//1024//1024//1024)))
    log.append('Source File Count:\t\t{:>12}'.format(str(filecount_src[i])))
    log.append('Destination File Count:\t{:>12}'.format(str(filecount_dst[i])))
    log.append('\n')

# End
stop = default_timer()
log.append("[LOG] Total Operation Time: " + str(stop - start) + " seconds\n")
export_log(log, log_path)
print("[LOG] Total Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing {0}\n".format(Path(argv[0]).name))

'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
https://docs.python.org/3/library/stat.html
https://stackoverflow.com/questions/8234445/format-output-string-right-alignment
'''
