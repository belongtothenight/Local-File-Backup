from logging import root
from os import system, getcwd
from os.path import basename, dirname, join
from pathlib import Path
from timeit import default_timer
from sys import argv
from lfb_lib import archive_single_file, disk_size_check, get_file_info, get_folder_info, disk_size_check, copy_file, archive_single_file, archive_folder, unpack_file, export_file_log, export_log, generate_process_file
from tkinter import *

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
dst_3 = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/set_process/'

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
    True,  # src file log flag associate with functions
    True,  # file log file of random location
    True,  # execution log flag
]

# Function Enable Array
function_enable = [
    ['Single_file_copy', True],  # single file copy
    ['Single_folder_copy', True],  # single folder copy
    ['Multi_folder_copy', True],  # multi file copy
    ['Single_file_archive', True],  # single file archive
    ['Single_folder_archive', True],  # single folder archive
    ['Multi_folder_archive', True],  # multi file archive
    ['Single_file_unpack', True],  # single file unpack
    ['Single_folder_unpack', True],  # single folder unpack
    ['Multi_folder_unpack', True]  # multi file unpack
]

# Process Array
log_path = 'D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/log/'
src_a = 'D:/Computer File/'
src_b = 'D:/Note_Database/'
dst_a = 'E:/Computer File/'
dst_b = 'F:/Computer File/'
dst_c = 'F:/N_D BackUp/Partial Copy of ND 20220805/'
dst_d = 'E:/N_D BackUp/Partial Copy of ND 20220805/'
dst_e = 'F:/Note_Database/'
process = [
    [2, 'CF Backup My Passport', src_a, dst_b],
    [2, 'CF Backup Transend', src_a, dst_a],
    [2, 'ND Backup My Passport', src_b, dst_c],
    [2, 'ND Backup Transend', src_b, dst_d],
    [2, 'ND Full Backup My Passport', src_b, dst_e]
]


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
# filename = function_enable[2][0]
# src_path = src_8
# dst_path = dst_2
# file_info, log = get_file_info(
#     src_path, dst_path, log, filter_1, print_flag[2])
# if file_log_flag[0]:
#     export_file_log(filename, file_info, dst_path)
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
# filter_1[2][1] = src_path
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
# filename = function_enable[8][0]
# src_path = dst_2
# dst_path = dst_2
# type = 'zip'  # zip, tar, gztar, bztar, xztar
# file_info, log = get_file_info(src_path, dst_path, log, filter_1, print_flag[2])
# if file_log_flag[0]:
#     export_file_log(filename, file_info, dst_path)
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
#     export_file_log(filename, file_info, dst_path)

'''Process File Generation'''
# filename = 'process_1'
# filetype = 'lfbp'
# dst_path = dst_3
# encoding = 'utf-8'
# content = ['process_1']
# content.append('===========================================================')
# content.append('<<Output Settings>>')
# content.append('Print_Main||{0}'.format(print_flag[0]))
# content.append('Print_Process||{0}'.format(print_flag[1]))
# content.append('Print_Sub_Function||{0}'.format(print_flag[2]))
# content.append('Export_SRC_File_Log||{0}'.format(file_log_flag[0]))
# content.append('Export_File_Log||{0}'.format(file_log_flag[1]))
# content.append('Export_Execution_Log||{0}'.format(file_log_flag[2]))
# content.append('===========================================================')
# content.append('<<Filter File Settings>>')
# content.append('Filter_file||{0}'.format(filter_1[0]))
# filter_str = ''
# for i in filter_1[1]:
#     filter_str += '||{0}'.format(i)
# content.append('Filter_File_Extension{0}'.format(filter_str))
# filter_str = ''
# for i in filter_1[2][0]:
#     filter_str += '||{0}'.format(i)
# content.append('Filter_File_Included_Words{0}'.format(filter_str))
# filter_str = ''
# for i in filter_1[2][1]:
#     filter_str += '||{0}'.format(i)
# content.append('Filter_File_Fullname{0}'.format(filter_str))
# content.append('Filter_File_Min_Size||{0}'.format(filter_1[3][0]))
# content.append('Filter_File_Max_Size||{0}'.format(filter_1[3][1]))
# content.append('Filter_File_Min_ATime||{0}'.format(filter_1[4][0]))
# content.append('Filter_File_Max_ATime||{0}'.format(filter_1[4][1]))
# content.append('Filter_File_Min_MTime||{0}'.format(filter_1[5][0]))
# content.append('Filter_File_Max_MTime||{0}'.format(filter_1[5][1]))
# content.append('Filter_File_Min_CTime||{0}'.format(filter_1[6][0]))
# content.append('Filter_File_Max_CTime||{0}'.format(filter_1[6][1]))
# content.append('===========================================================')
# content.append('<<Filter Folder Settings>>')
# content.append('Filter_Folder||{0}'.format(filter_2[0]))
# content.append('Filter_Folder_Extension||Not Implemented')
# filter_str = ''
# for i in filter_2[2][0]:
#     filter_str += '||{0}'.format(i)
# content.append('Filter_Folder_Included_Words{0}'.format(filter_str))
# filter_str = ''
# for i in filter_2[2][1]:
#     filter_str += '||{0}'.format(i)
# content.append('Filter_Folder_Fullname{0}'.format(filter_str))
# content.append('Filter_Folder_Min_Size||Not Implemented')
# content.append('Filter_Folder_Max_Size||Not Implemented')
# content.append('Filter_Folder_Min_ATime||{0}'.format(filter_2[4][0]))
# content.append('Filter_Folder_Max_ATime||{0}'.format(filter_2[4][1]))
# content.append('Filter_Folder_Min_MTime||{0}'.format(filter_2[5][0]))
# content.append('Filter_Folder_Max_MTime||{0}'.format(filter_2[5][1]))
# content.append('Filter_Folder_Min_CTime||{0}'.format(filter_2[6][0]))
# content.append('Filter_Folder_Max_CTime||{0}'.format(filter_2[6][1]))
# content.append('===========================================================')
# content.append('<<Process Settings>>')
# for i in function_enable:
#     content.append('{0}||{1}'.format(
#         i[0], i[1]))
# content.append('===========================================================')
# content.append('<<Process List>>')
# for i in process:
#     j = i[0]
#     content.append('{0}||{1}||{2}||{3}'.format(
#         function_enable[j][0], i[1], i[2], i[3]))
# content.append('===========================================================')
# log = generate_process_file(filename, filetype, dst_path, encoding, content, log)

'''Routine Execution Script Generation'''
'''
Description:
    Generate a script file to execute the process file.
# '''
# filename = 'routine_execution_script'
# filetype = 'py'
# dst_path = dst_3
# encoding = None
# py_dir = join(getcwd(), 'src\\')
# content = [
#     '# This is a Python Script in order to trigger program executed in routine mode\n']
# '''Routine Execution Script'''
# content.append('from os import system, chdir')
# content.append('p = \"{0}\"'.format(py_dir.replace('\\', '/')))
# content.append('fn = \"{0}\"'.format(basename(argv[0])))
# content.append('arg1 = \"routine_execution\"')
# content.append('system(\"cls\")')
# content.append('chdir(p)')
# content.append('system(\"python \" + fn + \" \" + arg1)')
# log = generate_process_file(
#     filename, filetype, dst_path, None, content, log)


def routine_execution():
    print('Python Script: {0} Executed in Routine Mode'.format(argv[0]))
    # Can include multiprocessing here
    # Dynamic variable for progress updating (local variable/object returned value from library)
    # tk.StringVar()


def normal_execution():
    print('[LOG] Python Script: {0} Executed'.format(argv[0]))
    '''Entry Window Setting'''
    entry_window = Tk()
    entry_window.geometry('960x540')
    entry_window.title('Local-File-Processor: Functionality Selection')
    # icon = PhotoImage(file='icon.png')
    # entry_window.iconphoto(True, icon)
    entry_window.config(background='#002EA4')
    entry_window.resizable(False, False)
    '''Entry Window Variable'''
    functionality_list = ['Copy', 'Archive', 'Unpack',
                          'File List Generator', 'Routine Execution Script Generator', 'Exit']
    '''Entry Window Function'''
    def set_functionality(value):
        # 1: Copy, 2: Archive, 3: Unpack, 4: File List Generator, 5: Routine Execution Script Generator
        global functionality
        functionality = value
        if print_flag[0]:
            print('[LOG] Choosed Functionality: {0}'.format(
                functionality_list[value-1]))
            entry_window.destroy()
    '''Widget'''
    canvas = Canvas(
        entry_window,
        bg="#002EA4",
        height=540,
        width=960,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )
    canvas.place(x=0, y=0)
    canvas.create_text(
        180,
        20,
        anchor="nw",
        text="Functionality Selection",
        fill="#FFFFFF",
        font=("ABeeZee", 40)
    )
    button_1 = Button(
        entry_window,
        text='COPY',
        font=("Consolas", 25, 'bold'),
        fg='#FFFFFF',
        bg='#002EA4',
        activeforeground='#002EA4',
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: set_functionality(1)
    )
    button_1.place(
        x=480,
        y=120,
        width=500.0,
        height=50.0,
        anchor="center"
    )
    button_2 = Button(
        entry_window,
        text='ARCHIVE',
        font=("Consolas", 25, 'bold'),
        fg='#FFFFFF',
        bg='#002EA4',
        activeforeground='#002EA4',
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: set_functionality(2)
    )
    button_2.place(
        x=480,
        y=170,
        width=500.0,
        height=50.0,
        anchor="center"
    )
    button_3 = Button(
        entry_window,
        text='UNPACK',
        font=("Consolas", 25, 'bold'),
        fg='#FFFFFF',
        bg='#002EA4',
        activeforeground='#002EA4',
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: set_functionality(3)
    )
    button_3.place(
        x=480,
        y=230,
        width=500.0,
        height=50.0,
        anchor="center"
    )
    button_4 = Button(
        entry_window,
        text='FILE LIST GENERATOR',
        font=("Consolas", 25, 'bold'),
        fg='#FFFFFF',
        bg='#002EA4',
        activeforeground='#002EA4',
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: set_functionality(4)
    )
    button_4.place(
        x=480,
        y=290,
        width=500.0,
        height=50.0,
        anchor="center"
    )
    button_5 = Button(
        entry_window,
        text='ROUTINE EXECUTION SCRIPT GENERATOR',
        font=("Consolas", 25, 'bold'),
        fg='#FFFFFF',
        bg='#002EA4',
        activeforeground='#002EA4',
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: set_functionality(5)
    )
    button_5.place(
        x=480,
        y=350,
        width=500.0,
        height=50.0,
        anchor="center"
    )
    button_6 = Button(
        entry_window,
        text='EXIT',
        font=("Consolas", 25, 'bold'),
        fg='#FFFFFF',
        bg='#002EA4',
        activeforeground='#002EA4',
        borderwidth=0,
        highlightthickness=0,
        relief="flat",
        command=lambda: set_functionality(6)
    )
    button_6.place(
        x=480,
        y=480,
        width=500.0,
        height=50.0,
        anchor="center"
    )
    '''Entry Window Display'''
    entry_window.mainloop()
    '''Function Windows'''
    # if functionality == 1:
    #     copy()
    # elif functionality == 2:
    #     archive()
    # elif functionality == 3:
    #     unpack()
    # elif functionality == 4:
    #     file_list_generator()
    # elif functionality == 5:
    #     routine_execution_script_generator()
    # elif functionality == 6:
    #     exit()
    # else:
    #     print('[ERROR] Functionality not selected')


if __name__ == '__main__':
    try:
        if argv[1] == 'routine_execution':
            # Executed with routine_execution argument
            routine_execution()
            # system('cmd /k')
    except IndexError:
        start = default_timer()
        system('cls')
        print("[LOG] Start executing {0}\n".format(Path(argv[0]).name))
        log = []
        normal_execution()
        stop = default_timer()
        log.append("[LOG] Total Operation Time: " +
                   str(stop - start) + " seconds\n")
        if file_log_flag[2]:
            export_log('log', log, src_8)
        if print_flag[0]:
            print("[LOG] Total Operation Time: " +
                  str(stop - start) + " seconds\n")
        print("[LOG] End executing {0}\n".format(Path(argv[0]).name))


'''
https://github.com/bnot elongtothenight/Local-File-Backup
https://docs.python.org/3/library/shutil.html
https://stackoverflow.com/questions/42487578/python-shutil-copytree-use-ignore-function-to-keep-specific-files-types
https://docs.python.org/3/library/stat.html
https://stackoverflow.com/questions/8234445/format-output-string-right-alignment
'''
