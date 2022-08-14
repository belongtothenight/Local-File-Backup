from concurrent.futures import process
from logging import root
from shutil import disk_usage, copy2, make_archive, unpack_archive, move, rmtree
from os import system, listdir, stat, walk, chdir, getcwd, sep, mkdir
from os.path import isfile, join, isdir, basename, dirname, exists
from pathlib import Path
from telnetlib import STATUS
from timeit import default_timer
from time import strftime, localtime
from datetime import date, datetime
from sys import argv
from multiprocessing import Process
from unittest import skip
from numpy import append

# Sub functions


def filter_file(file, filter):
    '''
    Args:
        file:   (str)   Full path of the file
        ---------- Filter ----------
        filter[0]:      (bool)      True if the file is to be filtered.
        ---------- File type ----------
        filter[1]:      (list/str)  File type   Extension       Exclude all files with these extension                              ['.txt', '.py']
        ---------- File name ----------
        filter[2][0]:   (list/str)  File name   Included words  Exclude all files with these words included in the name             ['te', 'st']
        filter[2][1]:   (list/str)  File name   Fullname        Exclude all files with these words excatly the same with the name   ['text.txt']
        ---------- File size ----------
        filter[3][0]:   (int)       File size   Min size        Exclude all files with size smaller than this value
        filter[3][1]:   (int)       File size   Max size        Exclude all files with size bigger than this value
        ---------- File atime ----------
        filter[4][0]:   (int)       File atime  Min atime       Exclude all files with atime smaller than this value
        filter[4][1]:   (int)       File atime  Max atime       Exclude all files with atime bigger than this value
        ---------- File mtime ----------
        filter[5][0]:   (int)       File mtime  Min mtime       Exclude all files with mtime smaller than this value
        filter[5][1]:   (int)       File mtime  Max mtime       Exclude all files with mtime bigger than this value
        ---------- File ctime ----------
        filter[6][0]:   (int)       File ctime  Min ctime       Exclude all files with ctime smaller than this value
        filter[6][1]:   (int)       File ctime  Max ctime       Exclude all files with ctime bigger than this value
    Returns:
        filter_flag: (bool) True if the file is filtered(excluded).
        filter_type: (str)  Filter type ('filter', 'type', 'name', 'size', 'atime', 'mtime', 'ctime')
    Description:
        This function filters the file with provided filter.
    '''
    filter_flag = False
    filter_type = ''
    # ---------- Filter ----------
    if filter[0] != True:
        filter_type = 'filter' + ' >> ' + str(filter[0])
        return filter_flag, filter_type
    # ---------- File type ----------
    if filter[1][0] != None:
        for element in filter[1]:
            if file.endswith(element):
                filter_flag = True
                filter_type = 'type' + ' >> ' + element
                return filter_flag, filter_type
    # ---------- File name ----------
    if filter[2][0][0] != None:
        for element in filter[2][0]:
            if basename(file).find(element) >= 0:
                filter_flag = True
                filter_type = 'name' + ' >> ' + element
                return filter_flag, filter_type
    if filter[2][1][0] != None:
        for element in filter[2][1]:
            if basename(file) == element:
                filter_flag = True
                filter_type = 'name' + ' >> ' + element
                return filter_flag, filter_type
    # ---------- File size ----------
    if filter[3][0] != None and filter[3][1] != None:
        if stat(file).st_size < filter[3][0] or stat(file).st_size > filter[3][1]:
            filter_flag = True
            filter_type = 'size' + ' >> ' + str(stat(file).st_size)
            return filter_flag, filter_type
    elif filter[3][0] != None:
        if stat(file).st_size < filter[3][0]:
            filter_flag = True
            filter_type = 'size' + ' >> ' + str(stat(file).st_size)
            return filter_flag, filter_type
    elif filter[3][1] != None:
        if stat(file).st_size > filter[3][1]:
            filter_flag = True
            filter_type = 'size' + ' >> ' + str(stat(file).st_size)
            return filter_flag, filter_type
    # ---------- File atime ----------
    if filter[4][0] != None and filter[4][1] != None:
        if stat(file).st_atime < filter[4][0] or stat(file).st_atime > filter[4][1]:
            filter_flag = True
            filter_type = 'atime' + ' >> ' + str(stat(file).st_atime)
            return filter_flag, filter_type
    elif filter[4][0] != None:
        if stat(file).st_atime < filter[4][0]:
            filter_flag = True
            filter_type = 'atime' + ' >> ' + str(stat(file).st_atime)
            return filter_flag, filter_type
    elif filter[4][1] != None:
        if stat(file).st_atime > filter[4][1]:
            filter_flag = True
            filter_type = 'atime' + ' >> ' + str(stat(file).st_atime)
            return filter_flag, filter_type
    # ---------- File mtime ----------
    if filter[5][0] != None and filter[5][1] != None:
        if stat(file).st_mtime < filter[5][0] or stat(file).st_mtime > filter[5][1]:
            filter_flag = True
            filter_type = 'mtime' + ' >> ' + str(stat(file).st_mtime)
            return filter_flag, filter_type
    elif filter[5][0] != None:
        if stat(file).st_mtime < filter[5][0]:
            filter_flag = True
            filter_type = 'mtime' + ' >> ' + str(stat(file).st_mtime)
            return filter_flag, filter_type
    elif filter[5][1] != None:
        if stat(file).st_mtime > filter[5][1]:
            filter_flag = True
            filter_type = 'mtime' + ' >> ' + str(stat(file).st_mtime)
            return filter_flag, filter_type
    # ---------- File ctime ----------
    if filter[6][0] != None and filter[6][1] != None:
        if stat(file).st_ctime < filter[6][0] or stat(file).st_ctime > filter[6][1]:
            filter_flag = True
            filter_type = 'ctime' + ' >> ' + str(stat(file).st_ctime)
            return filter_flag, filter_type
    elif filter[6][0] != None:
        if stat(file).st_ctime < filter[6][0]:
            filter_flag = True
            filter_type = 'ctime' + ' >> ' + str(stat(file).st_ctime)
            return filter_flag, filter_type
    elif filter[6][1] != None:
        if stat(file).st_ctime > filter[6][1]:
            filter_flag = True
            filter_type = 'ctime' + ' >> ' + str(stat(file).st_ctime)
            return filter_flag, filter_type
    return filter_flag, filter_type


def filter_folder(folder, filter):
    '''
    Args:
        folder:     (str) Full path of the folder.
        ---------- Filter ----------
        filter[0]:      (bool)      True if the file is to be filtered.
        ---------- Folder type ---------- (not implemented)
        filter[1]:      (list/str)  Folder type   Extension       Exclude all folders with these extension                              ['.txt', '.py']
        ---------- Folder name ----------
        filter[2][0]:   (list/str)  Folder name   Included words  Exclude all folders with these words included in the name             ['te', 'st']
        filter[2][1]:   (list/str)  Folder name   Fullname        Exclude all folders with these words excatly the same with the name   ['text.txt']
        ---------- Folder size ---------- (not implemented)
        filter[3][0]:   (int)       Folder size   Min size        Exclude all folders with size smaller than this value
        filter[3][1]:   (int)       Folder size   Max size        Exclude all folders with size bigger than this value
        ---------- Folder atime ----------
        filter[4][0]:   (int)       Folder atime  Min atime       Exclude all folders with atime smaller than this value
        filter[4][1]:   (int)       Folder atime  Max atime       Exclude all folders with atime bigger than this value
        ---------- Folder mtime ----------
        filter[5][0]:   (int)       Folder mtime  Min mtime       Exclude all folders with mtime smaller than this value
        filter[5][1]:   (int)       Folder mtime  Max mtime       Exclude all folders with mtime bigger than this value
        ---------- Folder ctime ----------
        filter[6][0]:   (int)       Folder ctime  Min ctime       Exclude all folders with ctime smaller than this value
        filter[6][1]:   (int)       Folder ctime  Max ctime       Exclude all folders with ctime bigger than this value
    Returns:
        filter_flag: (bool) True if the folder is filtered(excluded).
        filter_type: (str)  Filter type ('filter', 'type', 'name', 'size', 'atime', 'mtime', 'ctime')
    Description:
        This function filters the folder.
    '''
    filter_flag = False
    filter_type = ''
    # ---------- Filter ----------
    if filter[0] != True:
        filter_type = 'filter' + ' >> ' + str(filter[0])
        return filter_flag, filter_type
    # ---------- Folder type ---------- (not implemented)
    # ---------- Folder name ----------
    if filter[2][0][0] != None:
        for element in filter[2][0]:
            if basename(folder).find(element) >= 0:
                filter_flag = True
                filter_type = 'name' + ' >> ' + element
                return filter_flag, filter_type
    if filter[2][1][0] != None:
        for element in filter[2][1]:
            if basename(folder) == element:
                filter_flag = True
                filter_type = 'name' + ' >> ' + element
                return filter_flag, filter_type
    # ---------- Folder size ---------- (not implemented)
    # ---------- Folder atime ----------
    if filter[4][0] != None and filter[4][1] != None:
        if stat(folder).st_atime < filter[4][0] or stat(folder).st_atime > filter[4][1]:
            filter_flag = True
            filter_type = 'atime' + ' >> ' + str(stat(folder).st_atime)
            return filter_flag, filter_type
    elif filter[4][0] != None:
        if stat(folder).st_atime < filter[4][0]:
            filter_flag = True
            filter_type = 'atime' + ' >> ' + str(stat(folder).st_atime)
            return filter_flag, filter_type
    elif filter[4][1] != None:
        if stat(folder).st_atime > filter[4][1]:
            filter_flag = True
            filter_type = 'atime' + ' >> ' + str(stat(folder).st_atime)
            return filter_flag, filter_type
    # ---------- Folder mtime ----------
    if filter[5][0] != None and filter[5][1] != None:
        if stat(folder).st_mtime < filter[5][0] or stat(folder).st_mtime > filter[5][1]:
            filter_flag = True
            filter_type = 'mtime' + ' >> ' + str(stat(folder).st_mtime)
            return filter_flag, filter_type
    elif filter[5][0] != None:
        if stat(folder).st_mtime < filter[5][0]:
            filter_flag = True
            filter_type = 'mtime' + ' >> ' + str(stat(folder).st_mtime)
            return filter_flag, filter_type
    elif filter[5][1] != None:
        if stat(folder).st_mtime > filter[5][1]:
            filter_flag = True
            filter_type = 'mtime' + ' >> ' + str(stat(folder).st_mtime)
            return filter_flag, filter_type
    # ---------- Folder ctime ----------
    if filter[6][0] != None and filter[6][1] != None:
        if stat(folder).st_ctime < filter[6][0] or stat(folder).st_ctime > filter[6][1]:
            filter_flag = True
            filter_type = 'ctime' + ' >> ' + str(stat(folder).st_ctime)
            return filter_flag, filter_type
    elif filter[6][0] != None:
        if stat(folder).st_ctime < filter[6][0]:
            filter_flag = True
            filter_type = 'ctime' + ' >> ' + str(stat(folder).st_ctime)
            return filter_flag, filter_type
    elif filter[6][1] != None:
        if stat(folder).st_ctime > filter[6][1]:
            filter_flag = True
            filter_type = 'ctime' + ' >> ' + str(stat(folder).st_ctime)
            return filter_flag, filter_type
    return filter_flag, filter_type


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


def archive_extension(archive_format):
    '''
    Args:
        archive_format: (str) archive format ('zip', 'tar', 'gztar', 'bztar', 'xztar')
    Returns:
        archive_extension: (str) archive extension ('.zip', '.tar', '.tar.gz', '.tar.bz2', '.tar.xz')
    Description:
        This function checks if the archive format is valid.
    '''
    match (archive_format):
        case ('zip'):
            archive_extension = '.zip'
        case ('tar'):
            archive_extension = '.tar'
        case ('gztar'):
            archive_extension = '.tar.gz'
        case ('bztar'):
            archive_extension = '.tar.bz2'
        case ('xztar'):
            archive_extension = '.tar.xz'
    return archive_extension

# Main functions


def get_file_info(src_path, dst_path, log, filter, print_sub_flag):
    '''
    Args:
        src_path: (str) source path
        dst_path: (str) destination path
        log: (list) log list
        filter: (list) filter list
    Returns:
        values[0] fd_src:       (list)  source file         directory
        values[1] err_src:      (list)  source file         error
        values[2] size_src:     (list)  source file         size
        values[3] atime_src:    (list)  source file         access time
        values[4] mtime_src:    (list)  source file         modification time
        values[5] ctime_src:    (list)  source file         creation time
        values[6] fd_dst:       (list)  destination file    directory
        values[7] err_dst:      (list)  destination file    error
        values[8] size_dst:     (list)  destination file    size
        values[9] atime_dst:    (list)  destination file    access time
        values[10] mtime_dst:   (list)  destination file    modification time
        values[11] ctime_dst:   (list)  destination file    creation time
        values[12] tfs_src:     (int)   source file         total file size accessed (bytes)
        values[13] tfs_dst:     (int)   destination file    total file size accessed (bytes)
        values[14] tfs:         (int)                       total file size accessed (bytes)
        values[15] total_src:   (int)   source file         total file size (bytes)
        values[16] used_src:    (int)   source file         used space (bytes)
        values[17] free_src:    (int)   source file         free space (bytes)
        values[18] total_dst:   (int)   destination file    total file size (bytes)
        values[19] used_dst:    (int)   destination file    used space (bytes)
        values[20] free_dst:    (int)   destination file    free space (bytes)
        values[21] total:       (int)                       total file size (bytes)
        values[22] used:        (int)                       total used space (bytes)
        values[23] free:        (int)                       total free space (bytes)
        values[24] root_fd_src: (str)   source path         root directory
        values[25] root_fd_dst: (str)   destination path    root directory
    Description:
        This function gets the file information of the source and destination paths. It also calculates the total file size accessed, total file size, used space and free space. It serves as a initiator for providing critical information to the other functions.
    '''
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

    def list_all_files(path, file_directory, error_message, file_size, atime, mtime, ctime, filter, print_sub_flag):
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
        Description:
            This function lists all files in the given path. It also gets the file size, access time, modification time and creation time.
        '''
        try:
            for f in listdir(path):
                if isfile(join(path, f)):
                    flag, type = filter_file(join(path, f), filter)
                    if flag != True:
                        file_directory.append(join(path, f))
                        file_size.append(stat(join(path, f)).st_size)
                        atime.append(datetime.fromtimestamp(
                            int(stat(join(path, f)).st_atime)))
                        mtime.append(datetime.fromtimestamp(
                            int(stat(join(path, f)).st_mtime)))
                        ctime.append(datetime.fromtimestamp(
                            int(stat(join(path, f)).st_ctime)))
                    else:
                        if print_sub_flag:
                            print("[LOG] Skipping file: " +
                                  join(path, f) + "\t\t[FILTER] " + type)
                        log.append("[LOG] Skipping file: " +
                                   join(path, f) + "\t\t[FILTER] " + type)
                elif isdir(join(path, f)):
                    list_all_files(join(path, f), file_directory, error_message,
                                   file_size, atime, mtime, ctime, filter)  # recursive call
                else:
                    if print_sub_flag:
                        print("[LOG] Unknown file type: " + join(path, f))
                    log.append("[LOG] Unknown file type: " + join(path, f))
        except Exception as e:
            error_message.append(str(e))
            if print_sub_flag:
                print("[LOG] Error: " + str(e) +
                      " when processing " + join(path, f))
            log.append("[LOG] Error: " + str(e) +
                       " when processing " + join(path, f))
        return file_directory, error_message, file_size, atime, mtime, ctime

    fd, err, size, atime, mtime, ctime = create()  # create empty lists
    fd_src, err_src, size_src, atime_src, mtime_src, ctime_src = list_all_files(
        src_path, fd, err, size, atime, mtime, ctime, filter, print_sub_flag)
    fd, err, size, atime, mtime, ctime = create()  # reset
    fd_dst, err_dst, size_dst, atime_dst, mtime_dst, ctime_dst = list_all_files(
        dst_path, fd, err, size, atime, mtime, ctime, filter, print_sub_flag)
    fd, err, size, atime, mtime, ctime = create()  # reset
    tfs_src = sum_file_size(size_src)
    tfs_dst = sum_file_size(size_dst)
    tfs = tfs_src + tfs_dst
    # this delete the variables
    del fd[:], err[:], size[:], atime[:], mtime[:], ctime[:]

    # Gather disk usge info
    total_src, used_src, free_src = disk_usage(src_path)
    total_dst, used_dst, free_dst = disk_usage(dst_path)
    total = total_src + total_dst
    used = used_src + used_dst
    free = free_src + free_dst

    # Include root directory
    root_fd_src = src_path
    root_fd_dst = dst_path

    # Return values
    values = [
        fd_src, err_src, size_src, atime_src, mtime_src, ctime_src, fd_dst, err_dst, size_dst, atime_dst, mtime_dst, ctime_dst,
        tfs_src, tfs_dst, tfs, total_src, used_src, free_src, total_dst, used_dst, free_dst, total, used, free,
        root_fd_src, root_fd_dst
    ]
    return values, log


def get_folder_info(src_path, dst_path, log, filter, print_sub_flag):
    '''
    Args:
        src_path: (str) source path
        dst_path: (str) destination path
    Returns:
        values[0]   file_d_src:     (list) source file      file directory
        values[1]   folder_d_src:   (list) source folder    folder directory
        values[2]   err_src:        (list) source folder    error message
        values[3]   size_src:       (list) source folder    size
        values[4]   atime_src:      (list) source folder    access time
        values[5]   mtime_src:      (list) source folder    modification time
        values[6]   ctime_src:      (list) source folder    change time
        values[7]   tfs_src:        (int)  source file      total file size accessed (bytes)
        values[8]   total_src:      (int)  source file      total file size (bytes)
        values[9]   used_src:       (int)  source file      used space (bytes)
        values[10]  free_src:       (int)  source file      free space (bytes)
        values[11]  total_dst:      (int)  destination file total file size (bytes)
        values[12]  used_dst:       (int)  destination file used space (bytes)
        values[13]  free_dst:       (int)  destination file free space (bytes)
        values[14]  total:          (int)                   total file size  (bytes)
        values[15]  used:           (int)                   used space (bytes)
        values[16]  free:           (int)                   free space (bytes)
        values[17]  root_fd_src:    (str) source path       root directory
        values[18]  root_fd_dst:    (str) destination path  root directory
    Description:
        This function gets the folder information of the source and destination path.
    '''
    file_d = []
    folder_d = []
    err = []
    size = []
    atime = []
    mtime = []
    ctime = []
    # Get file info

    def get_folder_info(path, file_d, err, size):
        try:
            for f in listdir(path):
                if isfile(join(path, f)):
                    file_d.append(join(path, f))
                    size.append(stat(join(path, f)).st_size)
                elif isdir(join(path, f)):
                    get_folder_info(join(path, f), file_d, err,
                                    size)
                else:
                    if print_sub_flag:
                        print("[LOG] Unknown file type: " + join(path, f))
                    log.append("[LOG] Unknown file type: " + join(path, f))
        except Exception as e:
            err.append(str(e))
            if print_sub_flag:
                print("[LOG] Error: " + str(e) +
                      " when processing " + join(path, f))
            log.append("[LOG] Error: " + str(e) +
                       " when processing " + join(path, f))
        return file_d, err, size
    # Get folder info
    try:
        for f in listdir(src_path):
            if isdir(join(src_path, f)):
                flag, type = filter_folder(join(src_path, f), filter)
                if flag != True:
                    folder_d.append(join(src_path, f))
                    atime.append(stat(join(src_path, f)).st_atime)
                    mtime.append(stat(join(src_path, f)).st_mtime)
                    ctime.append(stat(join(src_path, f)).st_ctime)
                    file_d, err, size = get_folder_info(
                        join(src_path, f), file_d, err, size)
                else:
                    if print_sub_flag:
                        print("[LOG] Skipping folder: " +
                              join(src_path, f) + "\t\t[FILTER] " + type)
                    log.append("[LOG] Skipping folder: " +
                               join(src_path, f) + "\t\t[FILTER] " + type)
    except Exception as e:
        if print_sub_flag:
            print("[LOG] Error: " + str(e) +
                  " when processing " + join(src_path, f))
        log.append("[LOG] Error: " + str(e) +
                   " when processing " + join(src_path, f))
    tfs_src = sum_file_size(size)
    total_src, used_src, free_src = disk_usage(src_path)
    total_dst, used_dst, free_dst = disk_usage(dst_path)
    total = total_src + total_dst
    used = used_src + used_dst
    free = free_src + free_dst
    root_fd_src = src_path
    root_fd_dst = dst_path
    values = [
        file_d, folder_d, err, size, atime, mtime, ctime, tfs_src, total_src, used_src, free_src,
        total_dst, used_dst, free_dst, total, used, free, root_fd_src, root_fd_dst
    ]
    return values, log


def disk_size_check(src_size, free_dst_disk_size, log, print_sub_flag):
    '''
    Args:
        src_size: (int) source file size (bytes)
        free_dst_disk_size: (int) destination free disk size (bytes)
    Returns:
        flag: (bool) True if the source file size is less than the free disk size
    Description:
        This function checks if the source file size is more than the free disk size of the destination.
    '''
    flag = True
    if src_size > free_dst_disk_size:
        flag = False
        if print_sub_flag:
            print(
                "[LOG] Source file size is more than the free disk size of the destination.")
        log.append(
            "[LOG] Error: File size is larger than free disk size of the destination")
    else:
        if print_sub_flag:
            print("[LOG] Passed disk size check!.")
        log.append("[LOG] Passed disk size check!")
    return flag, log


def copy_file(fd_src, size_src, atime_src, mtime_src, fd_dst, fd_dst_l, size_dst, atime_dst, mtime_dst, log, print_sub_flag):
    '''
    Args:
        fd_src: (str) file directory
        size_src: (str) file size
        atime_src: (str) access time
        mtime_src: (str) modification time
        fd_dst: (str) file directory (root)
        fd_dst_l: (list) file directory
        size_dst: (list) file size
        atime_dst: (list) access time
        mtime_dst: (list) modification time
        log: (list) list to be filled with log messages
    Returns:
        log: (list) log messages
        progress: (list) number of actions completed and total actions
    Description:
        This function copies a file from the source path to the destination path. It also logs the actions performed.
    '''
    # Add duplication to this function
    try:
        # File with same name in dst
        j = fd_dst_l.index(join(fd_dst, Path(fd_src).name))
        if print_sub_flag:
            print("[LOG] Find file: " + fd_src)
        if size_src == size_dst[j] and atime_src == atime_dst[j] and mtime_src == mtime_dst[j]:
            # File has the same metadata beside creation time
            if print_sub_flag:
                print("[LOG] File is the same, skip " + fd_src)
            log.append("[LOG] File is the same, skip copy\t\t" + fd_src)
        else:
            # File has different metadata
            if print_sub_flag:
                print("[LOG] File is different, copy " + fd_src)
            log.append("[LOG] File is different, copy\t\t" + fd_src)
            copy2(fd_src, fd_dst)
    except Exception as e:
        # File is not found in dst
        if print_sub_flag:
            print("[LOG] File is not found in dst, copy" + fd_src)
        log.append("[LOG] File is not found in dst, copy\t" + fd_src)
        copy2(fd_src, fd_dst)
    return log


def archive_single_file(archive_name, src_path, dst_path, archive_format, log):
    '''
    Args:
        archive_name: (str) archive name
        src_path: (str) source path (file path)
        dst_path: (str) destination path (folder path)
        format: (str) archive format ('zip', 'tar', 'gztar', 'bztar', 'xztar')
        log: (list) list to be filled with log messages
    Returns:
        log: (list) log messages
    Description:
        This function archives a single file and provide archive duplication protection. It's achived by creating a folder and archive the file based on the folder, and later delete the folder.
    '''
    src_path_base = dirname(src_path)
    temp_path = join(src_path_base, archive_name + '_temp')
    if exists(temp_path):
        skip
    else:
        mkdir(temp_path)
    copy2(src_path, temp_path)
    archive_folder(archive_name, temp_path, dst_path, archive_format, log)
    rmtree(temp_path, ignore_errors=True)
    return log


def archive_folder(archive_name, src_path, dst_path, archive_format, log, print_sub_flag):
    '''
    Args:
        archive_name: (str) archive name
        src_path: (str) source path
        dst_path: (str) destination path
        format: (str) archive format ('zip', 'tar', 'gztar', 'bztar', 'xztar')
        log: (list) list to be filled with log messages
    Returns:
        log: (list) log messages
    Description:
        This function archives the folder and provide archive duplication protection.
    '''
    # Format
    archive_ext = archive_extension(archive_format)

    # Replication protection
    files = []
    for (dirpath, dirnames, filenames) in walk(dst_path):
        files.extend(filenames)
        break
    if archive_name + archive_ext in files:
        log.append("[LOG] Archive already exists, skip archiving\t" +
                   dst_path + archive_name + archive_ext)
        if print_sub_flag:
            print("[LOG] Archive already exists, skip archiving\t" +
                  dst_path + archive_name + archive_ext)
        return log

    # Create archive
    t_1 = default_timer()
    dir = getcwd()
    chdir(src_path)
    make_archive(base_name=join(dst_path, archive_name),
                 format=archive_format, root_dir=src_path, base_dir='./')
    chdir(dir)
    t_2 = default_timer()
    log.append("[LOG] Archive {0}{1} created.\t\t\tTakes {2} seconds.\t{3}".format(
        archive_name, archive_ext, t_2-t_1, dst_path + archive_name + archive_ext))
    if print_sub_flag:
        print("[LOG] Archive {0}{1} created.\t\t\tTakes {2} seconds.\t{3}".format(
            archive_name, archive_ext, t_2-t_1, dst_path + archive_name + archive_ext))
    return log


def unpack_file(archive_name, src_path, dst_path, archive_format, log, print_sub_flag):
    '''
    Args:
        archive_name: (str) archive name
        src_path: (str) source path
        dst_path: (str) destination path
        archive_format: (str) archive format ('zip', 'tar', 'gztar', 'bztar', 'xztar')
        log: (list) list to be filled with log messages
    '''
    # Format
    archive_ext = archive_extension(archive_format)

    # Replication protection
    folders = []
    for (dirpath, dirnames, filenames) in walk(dst_path):
        folders.extend(dirnames)
        break
    if archive_name in folders:
        log.append("[LOG] Folder already exists, skip unpacking\t" +
                   dst_path + archive_name)
        if print_sub_flag:
            print("[LOG] Folder already exists, skip unpacking\t" +
                  dst_path + archive_name)
        return log

    # Unpack archive
    t_1 = default_timer()
    try:
        unpack_archive(join(src_path, archive_name + archive_ext),
                       join(dst_path, archive_name), archive_format)
    except Exception as e:
        log.append("[LOG] Unpack archive failed\t\t\t" + "\t" + str(e))
        if print_sub_flag:
            print("[LOG] Unpack archive failed\t\t\t" + "\t" + str(e))
        return log
    t_2 = default_timer()
    log.append("[LOG] Archive {0}{1} unpacked.\t\t\tTakes {2} seconds.\t{3}".format(
        archive_name, archive_ext, t_2-t_1, dst_path + archive_name))
    if print_sub_flag:
        print("[LOG] Archive {0}{1} unpacked.\t\t\tTakes {2} seconds.\t{3}".format(
            archive_name, archive_ext, t_2-t_1, dst_path + archive_name))
    return log


def export_log(log, dst_path):
    '''
    Args:
        log: (list) log messages
        dst_path: (str) destination path
    Returns:
        None
    Description:
        Export log messages with file duplication protection
    '''
    # Filename duplication protection and generation
    files = []
    buf_1 = []
    buf_2 = []
    fcnt = []
    # Get all file name and generate new file number to avoid overwriting
    for (dirpath, dirnames, filenames) in walk(dst_path):
        files.extend(filenames)
        break
    for i in range(len(files)):
        buf_1 = files[i].split('_')
        buf_1 = list(buf_1[-1])
        for j in range(len(buf_1)):
            try:
                buf_2.append(int(buf_1[j]))
            except:
                continue
            buf_2 = [str(k) for k in buf_2]
            buf2 = ''.join(buf_2)
            fcnt.append(buf2)
        buf_2.clear()
    fcnt = [int(i) for i in fcnt]
    fcnt.sort()
    try:
        fcnt = fcnt[-1]+1
    except:
        fcnt = 1
    # Write to log file
    f = open(join(dst_path, 'log_{0}_{1}.txt'.format(
        str(date.today()), str(fcnt))), 'w', encoding='utf-8')
    for element in log:
        f.write(str(date.today()) + " " + strftime("%H:%M:%S",
                localtime()) + " " + element + "\n")
    f.close()


# Execution Warning
if __name__ == "__main__":
    system('cls')
    print("This is a module, not a script.")
