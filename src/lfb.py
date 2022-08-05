from logging import root
from os import system
from pathlib import Path
from timeit import default_timer
from sys import argv
from lfb_lib import archive_single_file, get_file_info, get_folder_info, copy_file, archive_single_file, archive_folder, unpack_file, export_log

# Variables
src_1 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/src/ffc.pyw'
src_2 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/src/'
src_3 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/'
src_4 = 'c:/'
src_5 = 'd:/'
src_6 = 'e:/'
src_7 = 'f:/'
src_8 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/log/'
dst_2 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/backup_test/dst/'

# Startup
start = default_timer()
system('cls')
print("[LOG] Start executing {0}\n".format(Path(argv[0]).name))
log = []

# Main
'''single_file_copy'''
# file_info = get_file_info(src_8, dst_2)
# i = file_info[0].index('D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/log/all_accessible_files_CD.txt')
# log = copy_file(
#     fd_src=file_info[0][i], size_src=file_info[2][i], 
#     atime_src=file_info[3][i], mtime_src=file_info[4][i], 
#     fd_dst=file_info[25], fd_dst_l=file_info[6], size_dst=file_info[8], 
#     atime_dst=file_info[9], mtime_dst=file_info[10], log=log
#     )
# del file_info[:]

'''single_folder_copy'''
# file_info = get_file_info(src_8, dst_2)
# progress = [0, len(file_info[0])]
# for i in range(len(file_info[0])):
#     log = copy_file(
#         fd_src=file_info[0][i], size_src=file_info[2][i], 
#         atime_src=file_info[3][i], mtime_src=file_info[4][i], 
#         fd_dst=file_info[25], fd_dst_l=file_info[6], size_dst=file_info[8], 
#         atime_dst=file_info[9], mtime_dst=file_info[10], log=log
#         )
#     progress[0] += 1
#     print("Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
# del file_info[:]

'''multi_folder_copy'''
# file_info = get_file_info(src_8, dst_2)
# progress = [0, len(file_info[0])]
# for i in range(len(file_info[0])):
#     log = copy_file(
#         fd_src=file_info[0][i], size_src=file_info[2][i], 
#         atime_src=file_info[3][i], mtime_src=file_info[4][i], 
#         fd_dst=file_info[25], fd_dst_l=file_info[6], size_dst=file_info[8], 
#         atime_dst=file_info[9], mtime_dst=file_info[10], log=log
#         )
#     progress[0] += 1
#     print("Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
# del file_info[:]

'''single_file_archive'''
# log = archive_single_file('test_ffc', src_1, dst_2, 'zip', log)
# log = archive_single_file('test_ffc', src_1, dst_2, 'tar', log)
# log = archive_single_file('test_ffc', src_1, dst_2, 'gztar', log)
# log = archive_single_file('test_ffc', src_1, dst_2, 'bztar', log)
# log = archive_single_file('test_ffc', src_1, dst_2, 'xztar', log)

'''single_folder_archive'''
# file_info = get_file_info(src_8, dst_2)
# log = archive_folder('test', file_info[24], file_info[25], 'zip', log)
# log = archive_folder('test', file_info[24], file_info[25], 'tar', log)
# log = archive_folder('test', file_info[24], file_info[25], 'gztar', log)
# log = archive_folder('test', file_info[24], file_info[25], 'bztar', log)
# log = archive_folder('test', file_info[24], file_info[25], 'xztar', log)
# del file_info[:]

'''multi_archive'''

'''single_file_unpack'''
# file_info = get_file_info(dst_2, dst_2)
# log = unpack_file('test', file_info[24], file_info[25], 'zip', log)
# log = unpack_file('test', file_info[24], file_info[25], 'tar', log)
# log = unpack_file('test', file_info[24], file_info[25], 'gztar', log)
# log = unpack_file('test', file_info[24], file_info[25], 'bztar', log)
# log = unpack_file('test', file_info[24], file_info[25], 'xztar', log)
# del file_info[:]

'''single_folder_unpack'''

'''multi_folder_unpack'''
# folder_info = get_folder_info(src_3, dst_2)
# progress = [0, len(folder_info[0])]
# for i in range(len(folder_info[0])):
#     log = archive_folder()
# del folder_info[:]

# End
stop = default_timer()
log.append("[LOG] Total Operation Time: " + str(stop - start) + " seconds\n")
export_log(log, src_8)
print("[LOG] Total Operation Time: " + str(stop - start) + " seconds\n")
print("[LOG] End executing {0}\n".format(Path(argv[0]).name))

'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
https://docs.python.org/3/library/stat.html
'''