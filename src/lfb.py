from logging import root
from os import system
from os.path import basename, dirname
from pathlib import Path
from timeit import default_timer
from sys import argv
from lfb_lib import archive_single_file, disk_size_check, get_file_info, get_folder_info, disk_size_check, copy_file, archive_single_file, archive_folder, unpack_file, export_log

# Path Variables
src_1 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/src/ffc.pyw'
src_2 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/src/'
src_3 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/'
src_4 = 'c:/'
src_5 = 'd:/'
src_6 = 'e:/'
src_7 = 'f:/'
src_8 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/log/'
src_9 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/log/all_accessible_files_CD.txt'
dst_2 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/dst/'

# Filter Array
filter_1 = [
    True,
    [None],  # ['.txt'],
    [['07-31'], ['log_2022-07-31_1.txt']],
    [16000, 48000],
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None]  # use time.mktime(9-tuple) to generate time code
]  # for filter_file
filter_2 = [
    True,
    None,  # not implemented
    [[None], ['src']],
    None,  # not implemented
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None],  # use time.mktime(9-tuple) to generate time code
    [None, None]  # use time.mktime(9-tuple) to generate time code
]  # for filter_folder

# Global Flag Variable
print_flag = [
    True,  # print in main
    True,  # print in processes of lib file
    True  # print in sub-functions of lib file
]
file_log_flag = [
    False,  # src file log flag associate with functions
    True,  # file log file of random location
    True,  # execution log flag
]

# Startup
start = default_timer()
system('cls')
print("[LOG] Start executing {0}\n".format(Path(argv[0]).name))
log = []

# Main
'''single_file_copy'''
# src_path_file = src_8
# dst_path = dst_2
# src_path = dirname(src_path_file)
# filter_1[2][1] = src_path_file
# file_info, log = get_file_info(
#     src_path, dst_path, log, filter_1, print_flag[2])
# flag, log = disk_size_check(file_info[12], file_info[20], log, print_flag[2])
# if flag:
#     log = copy_file(
#         fd_src=file_info[0][0], size_src=file_info[2][0],
#         atime_src=file_info[3][0], mtime_src=file_info[4][0],
#         fd_dst=file_info[25], fd_dst_l=file_info[6], size_dst=file_info[8],
#         atime_dst=file_info[9], mtime_dst=file_info[10], log=log, print_sub_flag=print_flag[2]
#     )
# del file_info[:], src_path, dst_path

'''single_folder_copy'''
# src_path = src_8
# dst_path = dst_2
# file_info, log = get_file_info(
#     src_path, dst_path, log, filter_1, print_flag[2][2])
# flag, log = disk_size_check(file_info[12], file_info[20], log, print_flag[2])
# if flag:
#     progress = [0, len(file_info[0])]
#     for i in range(len(file_info[0])):
#         log = copy_file(
#             fd_src=file_info[0][i], size_src=file_info[2][i],
#             atime_src=file_info[3][i], mtime_src=file_info[4][i],
#             fd_dst=file_info[25], fd_dst_l=file_info[6], size_dst=file_info[8],
#             atime_dst=file_info[9], mtime_dst=file_info[10], log=log, print_sub_flag=print_flag[2]
#         )
#         progress[0] += 1
#         if print_flag[1]:
#             print(
#                 "Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
# del file_info[:], src_path, dst_path

'''multi_folder_copy'''
# src_path = src_8
# dst_path = dst_2
# file_info, log = get_file_info(
#     src_path, dst_path, log, filter_1, print_flag[2])
# if file_log_flag[0]:
#     export_log(basename(src_path), file_info[0], dst_path)
# flag, log = disk_size_check(
#     file_info[12], file_info[20], log, print_flag[2])
# if flag:
#     progress = [0, len(file_info[0])]
#     for i in range(len(file_info[0])):
#         log = copy_file(
#             fd_src=file_info[0][i], size_src=file_info[2][i],
#             atime_src=file_info[3][i], mtime_src=file_info[4][i],
#             fd_dst=file_info[25], fd_dst_l=file_info[6], size_dst=file_info[8],
#             atime_dst=file_info[9], mtime_dst=file_info[10],
#             log=log, print_sub_flag=print_flag[1]
#         )
#         progress[0] += 1
#         if print_flag[1]:
#             print(
#                 "Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
# del file_info[:], src_path, dst_path

'''single_file_archive'''
# filename = 'test_ffc'
# src_path = src_1
# dst_path = dst_2
# type = 'zip' # zip, tar, gztar, bztar, xztar
# log = archive_single_file(filename, src_path, dst_path, type, log)
# del filename, src_path, dst_path, type

'''single_folder_archive'''
# filename = 'test'
# src_path = src_8
# dst_path = dst_2
# type = 'zip'  # zip, tar, gztar, bztar, xztar
# file_info, log = get_file_info(
#     src_path, dst_path, log, filter_1, print_flag[2])
# flag, log = disk_size_check(file_info[12], file_info[20], log, print_flag[2])
# if flag:
#     # choose one format
#     log = archive_folder(
#         'test', file_info[24], file_info[25], 'zip', log, print_flag[2])
# del file_info[:], filename, src_path, dst_path, type

'''multi_archive'''
# src_path = src_3
# dst_path = dst_2
# type = 'zip'  # zip, tar, gztar, bztar, xztar
# folder_info, log = get_folder_info(
#     src_path, dst_path, log, filter_2, print_flag[2])
# if file_log_flag[0]:
#     export_log(basename(src_path), folder_info[1], dst_path)
# flag, log = disk_size_check(
#     folder_info[7], folder_info[13], log, print_flag[2])
# if flag:
#     progress = [0, len(folder_info[1])]
#     for i in range(len(folder_info[1])):
#         log = archive_folder(
#             basename(folder_info[1][i]), folder_info[1][i], folder_info[18], type, log, print_flag[2])
#         progress[0] += 1
#         if print_flag[1]:
#             print(
#                 "Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
# del folder_info[:], src_path, dst_path, type

'''single_file_unpack'''
# filename = 'test'
# src_path = dst_2
# dst_path = dst_2
# type = 'zip'  # zip, tar, gztar, bztar, xztar
# file_info, log = get_file_info(
#     src_path, dst_path, log, filter_1, print_flag[2])
# flag, log = disk_size_check(file_info[12], file_info[20], log, print_flag[2])
# if flag:
#     log = unpack_file(filename, file_info[24],
#                       file_info[25], type, log, print_flag[2])
# del file_info[:], filename, src_path, dst_path, type

'''single_folder_unpack'''
# src_path = dst_2
# dst_path = dst_2
# type = 'zip'  # zip, tar, gztar, bztar, xztar
# file_info, log = get_file_info(
#     src_path, dst_path, log, filter_1, print_flag[2])
# flag, log = disk_size_check(file_info[12], file_info[20], log, print_flag[2])
# if flag:
#     progress = [0, len(file_info[0])]
#     for i in range(progress[1]):
#         if file_info[0][i].endswith(type):
#             log = unpack_file(basename(file_info[0][i]).rstrip(
#                 type), file_info[24], file_info[25], type, log, print_flag[2])
#             progress[0] += 1
#             if print_flag[1]:
#                 print(
#                     "Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
# del file_info[:], src_path, dst_path, type

'''multi_folder_unpack'''
# src_path = dst_2
# dst_path = dst_2
# type = 'zip'  # zip, tar, gztar, bztar, xztar
# file_info, log = get_file_info(src_path, dst_path, log, filter_1, print_flag[2])
# if file_log_flag[0]:
#     export_log(basename(src_path), file_info[0], dst_path)
# flag, log = disk_size_check(file_info[12], file_info[20], log, print_flag[2])
# if flag:
#     progress = [0, len(file_info[0])]
#     for i in range(progress[1]):
#         if file_info[0][i].endswith(type):
#             log = unpack_file(basename(file_info[0][i]).rstrip(
#                 type), dirname(file_info[0][i]), file_info[25], type, log, print_flag[2])
#             progress[0] += 1
#             if print_flag[1]:
#                 print(
#                     "Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
# del file_info[:]

'''file_log'''
# filename = 'test'
# location = src_3
# dst_path = dst_2
# file_info, log = get_file_info(location, dst_path, log, [None], print_flag[2])
# if file_log_flag[1]:
#     export_log(filename, file_info[0], dst_path)

# End
stop = default_timer()
log.append("[LOG] Total Operation Time: " + str(stop - start) + " seconds\n")
if file_log_flag[2]:
    export_log('log', log, src_8)
if print_flag[0]:
    print("[LOG] Total Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing {0}\n".format(Path(argv[0]).name))

'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
https://docs.python.org/3/library/stat.html
https://stackoverflow.com/questions/8234445/format-output-string-right-alignment
'''
