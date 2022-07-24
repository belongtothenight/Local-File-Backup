# Local File Backup
## ATTENTION: Under development
## Functionality
This is designed to do one side backup.
1. File Backup
2. File Filter
   1. File type
   2. Date Created
   3. File name
   4. Existed file replace?
3. Generate Execution Log</br>
	Record every file transfer.
4. Set Backup Process (Personal)</br>
	Execute backup process without any manual operation needed with pre-specified directory set.
	1. Full ND Backup My Passport
	2. ND Backup Transend
	3. ND Backup My Passport
	4. CF Backup Transend
	5. CF Backup My Passport
	6. Minecraft saves Backup
	7. Minecraft saves Backup zip
## GUI
1. Manual Operation
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
	   1. Progress bar
	   2. Show realtime log
	   3. Store log in csv file
2. Set Backup Process generation.</br>
   generate .py file(set in task scheduler) and a process csv file(record the backup exceptions), manually setup automatically execute by task scheduler</br>
   https://www.youtube.com/watch?v=Q6aV0ra1Z5A
## Set Backup Process
Routinely run by windows task scheduler. </br>
File structure: .py + .csv
## Requirements
