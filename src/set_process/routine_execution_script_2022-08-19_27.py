# This is a Python Script in order to trigger program executed in routine mode

from os import system, chdir
p = "D:/Note_Database/Subject/CPDWG Custom Program Developed With Gidhub/Local-File-Backup/src/"
fn = "lfb.py"
arg1 = "routine_execution"
system("cls")
chdir(p)
system("python " + fn + " " + arg1)
