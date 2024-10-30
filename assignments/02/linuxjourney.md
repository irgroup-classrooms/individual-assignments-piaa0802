## 1.The Shell
### Exercise
Try some other Linux commands and see what they output:

*1.* $ date

*Output:* Tue Oct 29 11:47:39     2024

*2.* $ whoami

*Output:* pia9c
### Quiz
What should be outputted to the display when you type echo Hello World?

*Answer:* Hello World

## 2.pwd (Print Working Directory)
### Quiz
How do I find what directory you are currently in?

*Answer:* pwd

## 3.cd (Change Directory)
### Exercise
Run the cd command without any flags, where does it take you?

*Output:* It takes me to the same directory that i am already in, so nothing happens.
### Quiz
If you are in /home/pete/Pictures and wanted to go to /home/pete, what’s a good shortcut to use?

*Answer:* cd ..

## 4.ls (List Directories)
### Exercise
Run ls with different flags and see the output you receive.

*1.* ls -R:

*Output:* recursively list directory contents

*2.* ls -r:

*Output:* reverse order while sorting

*3.* ls -t:

*Output:* sort by modification time, newest first
### Quiz
What command would you use to see hidden files?

*Answer:* ls -a

## 5.touch
### Exercise
*1.* Create a new file

*Input:* $ touch piasfile

*2.* Note the timestamp

*Input:* $ ls -l piasfile

*Output:* -rw-r--r-- 1 pia9c 197609 0 Oct 29 12:27 piasfile

*3.* Touch the file and check the timestamp once again

*Input:* $ touch piasfile
         $ ls -l piasfile

*Output:* -rw-r--r-- 1 pia9c 197609 0 Oct 30 12:43 piasfile   
### Quiz
How do you create a file called myfile?

*Answer:* touch myfile

## 6.file
### Exercise
Run the file command on a few different directories and files and note the output.

*1.*

*Intput:* file piasfile

*Output:* piasfile: empty
### Quiz
What command can you use to find the file type of a file?

*Answer:* file

## 7.cat
### Exercise
Run cat on different files and directories. Then try to cat multiple files.

*1.*

*Intput:* $ cat piasfile

*Output:* 

*Intput:* $ cat test.txt

*Output:* Test test test Pia
### Quiz
What's a good way to see the contents of a file?

*Answer:* cat

## 8.less
### Exercise
Run the file command on a few different directories and files and note the output.

*1.*

*Intput:* file piasfile

*Output:* piasfile: empty
### Quiz
What command can you use to find the file type of a file?

*Answer:* file
