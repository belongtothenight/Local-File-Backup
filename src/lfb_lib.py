from concurrent.futures import process
from logging import root
from shutil import disk_usage, copy2, make_archive
from os import system, listdir, stat, walk
from os.path import isfile, join, isdir
from pathlib import Path
from timeit import default_timer
from time import strftime, localtime
from datetime import date, datetime
from sys import argv
from multiprocessing import Process
from numpy import append

def get_file_info(src_path, dst_path):
    '''
    Args:
        src_path: (str) source path
        dst_path: (str) destination path
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
        values[12] tfs_src:     (list)  source file         total file size accessed (bytes)
        values[13] tfs_dst:     (list)  destination file    total file size accessed (bytes)
        values[14] tfs:         (list)                      total file size accessed (bytes)
        values[15] total_src:   (list)  source file         total file size (bytes)
        values[16] used_src:    (list)  source file         used space (bytes)
        values[17] free_src:    (list)  source file         free space (bytes)
        values[18] total_dst:   (list)  destination file    total file size (bytes)
        values[19] used_dst:    (list)  destination file    used space (bytes)
        values[20] free_dst:    (list)  destination file    free space (bytes)
        values[21] total:       (list)                      total file size (bytes)
        values[22] used:        (list)                      total used space (bytes)
        values[23] free:        (list)                      total free space (bytes)
        values[24] root_fd_src: (str)   source path         root directory
        values[25] root_fd_dst: (str)   destination path    root directory
    Description:
        This function gets the file information of the source and destination paths. It also calculates the total file size accessed, total file size, used space and free space. It serves as a initiator for providing critical information to the other functions.
    '''
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
        Description:
            This function lists all files in the given path. It also gets the file size, access time, modification time and creation time.
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

    fd, err, size, atime, mtime, ctime = create() # create empty lists
    fd_src, err_src, size_src, atime_src, mtime_src, ctime_src = list_all_files(src_path, fd, err, size, atime, mtime, ctime)
    fd, err, size, atime, mtime, ctime = create() # reset
    fd_dst, err_dst, size_dst, atime_dst, mtime_dst, ctime_dst = list_all_files(dst_path, fd, err, size, atime, mtime, ctime)
    fd, err, size, atime, mtime, ctime = create() # reset
    tfs_src = sum_file_size(size_src)
    tfs_dst = sum_file_size(size_dst)
    tfs = tfs_src + tfs_dst
    del fd[:], err[:], size[:], atime[:], mtime[:], ctime[:] # this delete the variables

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
    return values

def copy_file(fd_src, size_src, atime_src, mtime_src, fd_dst, fd_dst_l, size_dst, atime_dst, mtime_dst, log):
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

    try:
        # File with same name in dst
        j = fd_dst_l.index(join(fd_dst, Path(fd_src).name))
        # print("[LOG] Find file: " + fd_src)
        if size_src==size_dst[j] and atime_src==atime_dst[j] and mtime_src==mtime_dst[j]:
            # File has the same metadata beside creation time
            # print("[LOG] File is the same, skip " + fd_src)
            log.append("[LOG] File is the same, skip copy\t\t" + fd_src)
        else:
            # File has different metadata
            # print("[LOG] File is different, copy " + fd_src)
            log.append("[LOG] File is different, copy\t\t" + fd_src)
            copy2(fd_src, fd_dst)
    except Exception as e:
        # File is not found in dst
        # print("[LOG] File is not found in dst, copy" + fd_src)
        log.append("[LOG] File is not found in dst, copy\t" + fd_src)
        copy2(fd_src, fd_dst)
    return log

def archive_folder(archive_name, src_path, dst_path, log, archive_format):
    '''
    Args:
        archive_name: (str) archive name
        src_path: (str) source path
        dst_path: (str) destination path
        log: (list) list to be filled with log messages
        format: (str) archive format ('zip', 'gztar')
    Returns:
        log: (list) log messages
    Description:
        This function archives the folder and provide archive replication protection.
    '''
    files = []
    # Formate
    match (archive_format):
        case ('zip'):
            archive_ext = '.zip'
        case ('tar'):
            archive_ext = '.tar'
        case ('gztar'):
            archive_ext = '.tar.gz'
        case ('bztar'):
            archive_ext = '.tar.bz2'
        case ('xztar'):
            archive_ext = '.tar.xz'

    # Replication protection
    for (dirpath, dirnames, filenames) in walk(dst_path):
        files.extend(filenames)
        break
    if archive_name + archive_ext in files:
        log.append("[LOG] Archive already exists, skip archiving\t" + dst_path + archive_name + archive_ext)
        print("[LOG] Archive already exists, skip archiving\t" + dst_path + archive_name + archive_ext)
        return log

    # Create archive
    t_1 = default_timer()
    make_archive(base_name=join(dst_path, archive_name), format=archive_format, root_dir=dst_path, base_dir=src_path)
    t_2 = default_timer()
    log.append("[LOG] Archive {0}{1} created.\t\t\tTakes {2} seconds.".format(archive_name, archive_ext, t_2-t_1))
    print("[LOG] Archive {0}{1} created.\t\t\tTakes {2} seconds.".format(archive_name, archive_ext, t_2-t_1))
    return log

def export_log(log, dst_path):
    '''
    Args:
        log: (list) log messages
        dst_path: (str) destination path
    Returns:
        None
    Description:
        Export log messages with file replication protection
    '''
    # Filename replication protection and generation
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
    f = open(join(dst_path, 'log_{0}_{1}.txt'.format(str(date.today()), str(fcnt))), 'w', encoding='utf-8')
    for element in log:
        f.write(str(date.today()) + " " + strftime("%H:%M:%S", localtime()) + " " + element + "\n")
    f.close()

if __name__ == "__main__":
    system('cls')
    print("This is a module, not a script.")