from concurrent.futures import process
from logging import root
from shutil import disk_usage, copy2, make_archive, unpack_archive, move, rmtree
from os import system, listdir, stat, walk, chdir, getcwd, sep, mkdir
from os.path import isfile, join, isdir, basename, dirname, exists
from pathlib import Path
from timeit import default_timer
from time import strftime, localtime
from datetime import date, datetime
from sys import argv
from multiprocessing import Process
from unittest import skip
from numpy import append

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

def get_folder_info(src_path, dst_path):
    '''
    Args:
        src_path: (str) source path
        dst_path: (str) destination path
    Returns:
        values[0]   file_d_src:     (list) source file      file directory
        values[1]   folder_d_src:   (list) source file      folder directory
        values[2]   err_src:        (list) source file      error message
        values[3]   size_src:       (list) source file      size
        values[4]   tfs_src:        (int)  source file      total file size accessed (bytes)
        values[5]   total_src:      (int)  source file      total file size (bytes)
        values[6]   used_src:       (int)  source file      used space (bytes)
        values[7]   free_src:       (int)  source file      free space (bytes)
        values[8]   total_dst:      (int)  destination file total file size (bytes)
        values[9]   used_dst:       (int)  destination file used space (bytes)
        values[10]   free_dst:       (int)  destination file free space (bytes)
        values[11]  total:          (int)                   total file size  (bytes)
        values[12]  used:           (int)                   used space (bytes)
        values[13]  free:           (int)                   free space (bytes)
        values[14]  root_fd_src:    (str) source path       root directory
        values[15]  root_fd_dst:    (str) destination path  root directory
    Description:
        This function gets the folder information of the source and destination path.
    '''
    file_d = []
    folder_d = []
    err = []
    size = []
    def get_folder_info(path, file_d, folder_d, err, size):
        try:
            for f in listdir(path):
                if isfile(join(path, f)):
                    file_d.append(join(path, f))
                    size.append(stat(join(path, f)).st_size)
                elif isdir(join(path, f)):
                    folder_d.append(join(path, f))
                    get_folder_info(join(path, f), file_d, folder_d, err, size)
                else:
                    print("[LOG] Unknown file type: " + join(path, f))
        except Exception as e:
            err.append(str(e))
            print("[LOG] Error: " + str(e))
        return file_d, folder_d, err, size
    file_d, folder_d, err, size = get_folder_info(src_path, file_d, folder_d, err, size)
    tfs_src = sum_file_size(size)
    total_src, used_src, free_src = disk_usage(src_path)
    total_dst, used_dst, free_dst = disk_usage(dst_path)
    total = total_src + total_dst
    used = used_src + used_dst
    free = free_src + free_dst
    root_fd_src = src_path
    root_fd_dst = dst_path
    values = [
        file_d, folder_d, err, size, tfs_src, total_src, used_src, free_src, 
        total_dst, used_dst, free_dst, total, used, free, root_fd_src, root_fd_dst
        ]
    return values
    # return value

def duplicate_file_check():
    print()

def duplicate_folder_check():
    print()

def disk_size_check():
    print()

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
    ## Add duplication to this function
    try:
        # File with same name in dst
        j = fd_dst_l.index(join(fd_dst, Path(fd_src).name))
        # print("[LOG] Find file: " + fd_src)
        if size_src==size_dst[j] and atime_src==atime_dst[j] and mtime_src==mtime_dst[j]:
            # File has the same metadata beside creation time
            print("[LOG] File is the same, skip " + fd_src)
            log.append("[LOG] File is the same, skip copy\t\t" + fd_src)
        else:
            # File has different metadata
            print("[LOG] File is different, copy " + fd_src)
            log.append("[LOG] File is different, copy\t\t" + fd_src)
            copy2(fd_src, fd_dst)
    except Exception as e:
        # File is not found in dst
        print("[LOG] File is not found in dst, copy" + fd_src)
        log.append("[LOG] File is not found in dst, copy\t" + fd_src)
        copy2(fd_src, fd_dst)
    return log

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

def archive_folder(archive_name, src_path, dst_path, archive_format, log):
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
        log.append("[LOG] Archive already exists, skip archiving\t" + dst_path + archive_name + archive_ext)
        print("[LOG] Archive already exists, skip archiving\t" + dst_path + archive_name + archive_ext)
        return log

    # Create archive
    t_1 = default_timer()
    dir = getcwd()
    chdir(src_path)
    make_archive(base_name=join(dst_path, archive_name), format=archive_format, root_dir=src_path, base_dir='./')
    chdir(dir)
    t_2 = default_timer()
    log.append("[LOG] Archive {0}{1} created.\t\t\tTakes {2} seconds.\t{3}".format(archive_name, archive_ext, t_2-t_1, dst_path + archive_name + archive_ext))
    print("[LOG] Archive {0}{1} created.\t\t\tTakes {2} seconds.\t{3}".format(archive_name, archive_ext, t_2-t_1, dst_path + archive_name + archive_ext))
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

def unpack_file(archive_name, src_path, dst_path, archive_format, log):
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
        log.append("[LOG] Folder already exists, skip unpacking\t" + dst_path + archive_name)
        print("[LOG] Folder already exists, skip unpacking\t" + dst_path + archive_name)
        return log

    # Unpack archive
    t_1 = default_timer()
    unpack_archive(join(src_path, archive_name + archive_ext), join(dst_path, archive_name), archive_format)
    t_2 = default_timer()
    log.append("[LOG] Archive {0}{1} unpacked.\t\t\tTakes {2} seconds.\t{3}".format(archive_name, archive_ext, t_2-t_1, dst_path + archive_name))
    print("[LOG] Archive {0}{1} unpacked.\t\t\tTakes {2} seconds.\t{3}".format(archive_name, archive_ext, t_2-t_1, dst_path + archive_name))
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
    f = open(join(dst_path, 'log_{0}_{1}.txt'.format(str(date.today()), str(fcnt))), 'w', encoding='utf-8')
    for element in log:
        f.write(str(date.today()) + " " + strftime("%H:%M:%S", localtime()) + " " + element + "\n")
    f.close()

if __name__ == "__main__":
    system('cls')
    print("This is a module, not a script.")