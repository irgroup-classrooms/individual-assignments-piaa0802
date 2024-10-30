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

## 8.less #!!!!!!!!!
### Exercise
Run the file command on a few different directories and files and note the output.

*1.*

*Intput:* file piasfile

*Output:* piasfile: empty
### Quiz
How do you quit out of a less command?

*Answer:* q

## 9.history
### Exercise
Navigate through your previous command history with the Up and Down keys. Play around with ctrl-R reverse search.

*1.*

*Intput:* $ history

*Output:*   

    1  date
    2  whoami
    3  cd
    4  cd
    5  cd.
    6  cd .
    7  ls -R
    8  touch piasfile
    9  -l piasfile
   10  -I piasfile
   11  ls -l piasfile
   12  touch
   13  ls -l piasfile
   14  touch piasfile
   15  ls -l piasfile
   16  file piasfile
   17  file Divisionstestverfahren
   18  cat test
   19  cat test.txt
   20  file test.txt
   21  file test
   22  cat piasfile
   23  less Trendprognose
   24  less Trendprognose.pdf
   25  less g Trendprognose.pdf
   26  history
### Quiz
What is the command to clear the terminal?

*Answer:* clear

## 10.cp (Copy)
### Exercise
Copy over a couple of files, be careful not to overwrite anything important.

*1.*

*Intput:* $ cat piasfile

*Output:* 

*Intput:* $ cat test.txt

*Output:* Test test test Pia
### Quiz
What flag do you need to specify to copy over a directory?

*Answer:* -r


