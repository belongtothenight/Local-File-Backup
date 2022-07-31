from logging import root
from os import system
from pathlib import Path
from timeit import default_timer
from sys import argv
from lfb_lib import get_file_info, copy_file, archive_folder, export_log

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

# Main
file_info = get_file_info(src_8, dst_2)
log = []
progress = [0, len(file_info[0])]
'''copy'''
for i in range(len(file_info[0])):
    log = copy_file(
        fd_src=file_info[0][i], size_src=file_info[2][i], 
        atime_src=file_info[3][i], mtime_src=file_info[4][i], 
        fd_dst=file_info[25], fd_dst_l=file_info[6], size_dst=file_info[8], 
        atime_dst=file_info[9], mtime_dst=file_info[10], log=log
        )
    progress[0] += 1
    print("Progress: {0}/{1}:\t{2}".format(progress[0], progress[1], log[-1]))
'''archive'''
log = archive_folder('test', file_info[24], file_info[25], log, 'zip')
log = archive_folder('test', file_info[24], file_info[25], log, 'tar')
log = archive_folder('test', file_info[24], file_info[25], log, 'gztar')
log = archive_folder('test', file_info[24], file_info[25], log, 'bztar')
log = archive_folder('test', file_info[24], file_info[25], log, 'xztar')

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