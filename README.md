# Local File Backup
## ATTENTION: Under development
## Functionality
This is designed to do one side backup.
1. [] File Backup
2. [] File Filter
   1. File type
   2. Date Created
   3. File name
   4. Existed file replace?
3. Generate Execution Log</br>
	Record every file transfer.
4. Generate Set Backup Process (Personal)</br>
	Can execute backup process without any manual operation needed with pre-specified directory set.</br>
	Routinely run by windows task scheduler. </br>
	File structure: .py(set in task scheduler) + .csv(record the backup exceptions)</br>
	https://www.youtube.com/watch?v=Q6aV0ra1Z5A
	1. Full ND Backup My Passport
	2. ND Backup Transend
	3. ND Backup My Passport
	4. CF Backup Transend
	5. CF Backup My Passport
	6. Minecraft saves Backup
	7. Minecraft saves Backup zip
## GUI
1. Select source and destination.
	1. Source Directory
	2. Destination Directory
	3. src and dst set selection.
2. View all copying files.
	1. Filtering
	2. Check and uncheck files
	3. View file list
	4. View process states
3. Backup.
    1. Set Backup Process generation.</br>
   		generate .py file and .csv file for routine execution.
       1. Show generated .py file
       2. Show generated .csv file
	2. Estimation Run.</br>
       1. Show rogress bar
       2. Show realtime log
	3. Backup.</br>
       1. Show progress bar
       2. Show realtime log
       3. Store log in csv file

## Requirements
