# Local File Backup
## ATTENTION: Under development
## Description
This repo aims to create a less complex version of backup softwares, but with the ability to automate the entire process.</br>
This project is heavily inspired by [SyncBack](https://www.2brightsparks.com/).
## Undergoing Work
1. [ ] Add unpack function
2. [ ] Add file filter inside get_file_info() function
3. [ ] Change the entire fully tested code into a function and move it to lib file
4. [ ] Add a read and write set_process functionality to the main file
```
lfb_process_processname.lfbp
===========================================================
Process Settings</br>
replica||False                                              (True: auto rename/False: ignore)
filter_on||True                                             (True: Enable/False: Disable) 
copy_single_on||True                                        (True: Enable/False: Disable)
copy_multi_on||True                                         (True: Enable/False: Disable)
archive_auto_rename||True									(True: Enable/False: Disable)
archive_single_on||True                                     (True: Enable/False: Disable)
archive_multi_on||True                                      (True: Enable/False: Disable)
unpack_auto_rename||True									(True: Enable/False: Disable)
unpack_single_on||True                                      (True: Enable/False: Disable)
unpack_multi_on||True                                       (True: Enable/False: Disable)
===========================================================
Exclude file filters
filter_filetype||txt                                       	(filetype)                                              (without dot)
filter_atime_after||2022-01-01 00:00:00                    	(YYYY-MM-DD HH:MM:SS)                                   (date + time)
filter_atime_before||2022-01-01 00:00:00                   	(YYYY-MM-DD HH:MM:SS)                                   (date + time)
filter_mtime_after||2022-01-01 00:00:00                    	(YYYY-MM-DD HH:MM:SS)                                   (date + time)
filter_mtime_before||2022-01-01 00:00:00                   	(YYYY-MM-DD HH:MM:SS)                                   (date + time)
filter_ctime_after||2022-01-01 00:00:00                    	(YYYY-MM-DD HH:MM:SS)                                   (date + time)
filter_ctime_before||2022-01-01 00:00:00                   	(YYYY-MM-DD HH:MM:SS)                                   (date + time)
filter_filename_exact||123                                 	(Filename without extension)                            (exact match filename)
filter_filenamePartial||12                                 	(Partial filename without extension)                    (partial match filename)
filter_file||D:/123.txt                                    	(Full path with file)                                   (exact match file)
filter_folder||D:/                                         	(Full path till folder)                                 (exact match folder)
===========================================================
Process List
copy_single_process||D:/1.txt||E:/                          (path||path)                                            (src path till file||dst path till folder)                                              Copy single file
copy_multi_process||D:/||E:/                                (path||path)                                            (src path till folder||dst path till folder)                                            Copy file tree
archive_single_process||D:/||E:/||test||gztar               (path||path||filename||zip/tar/gztar/bztar/xztar)       (src path till folder||dst path till folder||archive filename||archive filetype)        Archive the given folder and save it in the given destination folder.
archive_multi_process||D:/||E:/||Original||gztar            (path||path||Original/Auto||zip/tar/gztar/bztar/xztar)  (src path till folder||dst path till folder||foldername/Autonaming||archive filetype)   Archive the sub folders in given folder and save them in the given destination folder.
unpack_single_process||D:/||E:/||test||zip                  (path||path||filename||zip/tar/gztar/bztar/xztar)       (src path till folder||dst path till folder||archive filename||archive filetype)        Unpack the given archive file and save it in the given destination folder.
unpack_multi_process||D:/||E:/||test||zip                   (path||path||Original/Auto||zip/tar/gztar/bztar/xztar)  (src path till folder||dst path till folder||foldername/Autonaming||archive filetype)   Unpack the sub folders in given archive file and save them in the given destination folder.
===========================================================
```
5. [ ] Add GUI

## Functionality
1. File Backup
   1. [x] Single file backup
   2. [ ] Single folder backup
   3. [x] Multi folder backup
2. File Archive
   1. [x] Single file archive
   2. [ ] Single folder archive
   3. [ ] Multi folder archive
3. File Unpack
   1. [x] Single file unpack
   2. [ ] Single folder unpack
   3. [ ] Multi folder unpack
4. File Filter
   1. [ ] File type
   2. [ ] Date Created
   3. [ ] File name
   4. [ ] Replication check
5. Generate Execution Log</br>
	1. [x] Record every file transfer.
6. Generate Set Backup Process (Personal)</br>
	Can execute backup process without any manual operation needed with pre-specified directory set.</br>
	Routinely run by windows task scheduler. </br>
	File structure: .py(set in task scheduler) + .csv(record the backup exceptions)</br>
	https://www.youtube.com/watch?v=Q6aV0ra1Z5A
	1. [ ] Full ND Backup My Passport
	2. [ ] ND Backup Transend
	3. [ ] ND Backup My Passport
	4. [ ] CF Backup Transend
	5. [ ] CF Backup My Passport
	6. [ ] Minecraft saves Backup
	7. [ ] Minecraft saves Backup zip
## GUI
1. Select source and destination.
	1. [ ] Source Directory
	2. [ ] Destination Directory
	3. [ ] src and dst set selection.
2. View all copying files.
	1. [ ] Filtering
	2. [ ] Check and uncheck files
	3. [ ] View file list
	4. [ ] View process states
3. Backup.
    1. Set Backup Process generation.</br>
   		generate .py file and .csv file for routine execution.
       1. [ ] Show generated .py file
       2. [ ] Show generated .csv file
	2. Estimation Run.</br>
       1. [ ] Show rogress bar
       2. [ ] Show realtime log
	3. Backup.</br>
       1. [ ] Show progress bar
       2. [ ] Show realtime log
       3. [ ] Store log in csv file