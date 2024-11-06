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
Run less on a file, then page up and around the file. Try searching for a specific word. Quickly navigate to the beginning or the end of the file. 

*1.*

*Intput:* $ less /c/Users/pia9c/Test.txt
          $ g
          $ G

*Output:* Komplette File wird ausgegeben
          Es wird nach oben gescrollt
          Es wird nach unten gescrollt
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

*Intput:* $ cp test.txt /c/Uni/DIS11
### Quiz
What flag do you need to specify to copy over a directory?

*Answer:* -r

## 11.mv (Move) 
### Exercise
Rename a file, then move that file to a different directory.

*1.*

*Intput:* $ mv piasfile piasnewfile

*Output:* Name wurde geändert

*Intput:* $ mv piasnewfile /c/Uni/DIS08

*Output:* File wurde in entsprechenden Ordner verschoben
### Quiz
How do you rename a file called cat to dog?

*Answer:* mv cat dog

## 12.mkdir (Make Directory)
### Exercise
Make a couple of directories and move some files into that directory.

*1.*

*Intput:* $ mkdir -p /c/Uni/DIS08/TestDirectory

*Output:* TestDirectory ist jetzt im Ordner DIS08

*Intput:* $ mv Test2.txt /c/Uni/DIS08/TestDirectory

*Output:* Test" ist jetzt in TestDirectory
### Quiz
What command is use to make a directory?

*Answer:* mkdir

## 13.rm (remove) 
### Exercise
Create a file called -file (don't forget the dash!).
Remove that file.

*1.*

*Intput:* $ touch -file

*Output:* File created

*2.*

*Intput:* $ rm -file

*Output:* File removed
### Quiz
How do you remove a file called myfile?

*Answer:* rm myfile

## 14.find
### Exercise
Find a file from the root directory that has the word net in it.

*1.*

*Intput:* $ find /c/Users -name net

*Output:* /c/Users/pia9c/anaconda3/Library/include/aws/core/net

### Quiz
What option should I specify for find if I want to search by name?

*Answer:* -name

## 15.help
### Exercise
Run help on the echo command, logout command and pwd command.

*1.*

*Intput:* $ help echo

*Output:* 

echo: echo [-neE] [arg ...]
    Write arguments to the standard output.

    Display the ARGs, separated by a single space character and followed by a
    newline, on the standard output.

    Options:
      -n        do not append a newline
      -e        enable interpretation of the following backslash escapes
      -E        explicitly suppress interpretation of backslash escapes

    `echo' interprets the following backslash-escaped characters:
      \a        alert (bell)
      \b        backspace
      \c        suppress further output
      \e        escape character
      \E        escape character
      \f        form feed
      \n        new line
      \r        carriage return
      \t        horizontal tab
      \v        vertical tab
      \\        backslash
      \0nnn     the character whose ASCII code is NNN (octal).  NNN can be
                0 to 3 octal digits
      \xHH      the eight-bit character whose value is HH (hexadecimal).  HH
                can be one or two hex digits
      \uHHHH    the Unicode character whose value is the hexadecimal value HHHH.
                HHHH can be one to four hex digits.
      \UHHHHHHHH the Unicode character whose value is the hexadecimal value
                HHHHHHHH. HHHHHHHH can be one to eight hex digits.

    Exit Status:
    Returns success unless a write error occurs.

*2.*

*Intput:* $ help logout

*Output:* 

logout: logout [n]
    Exit a login shell.

    Exits a login shell with exit status N.  Returns an error if not executed
    in a login shell.

*3.*

*Intput:* $ help pwd

*Output:* 

pwd: pwd [-LPW]
    Print the name of the current working directory.

    Options:
      -L        print the value of $PWD if it names the current working
                directory
      -P        print the physical directory, without any symbolic links
      -W        print the Win32 value of the physical directory

    By default, `pwd' behaves as if `-L' were specified.

    Exit Status:
    Returns 0 unless an invalid option is given or the current directory
    cannot be read.


### Quiz
How do you get quick command line help for built-in bash commands?

*Answer:* help

## 16.man 
### Exercise
Run the man command on the ls command.

*1.*

*Intput:* $ man ls

*Output:* manuel opened

### Quiz
How do you see the manuals for a command?

*Answer:* man

## 17.whatis 
### Exercise
Run the whatis command on the less command.

*1.*

*Intput:* $ whatis less

*Output:* Brief describtion of less

### Quiz
What command can you use to see a small description of a command?

*Answer:* whatis

## 18.alias
### Exercise
Create a couple of aliases then remove them.

*1.*

*Intput:* $ $ alias foobar='ls -la'

*Output:* ls -la ist jetzt ~

*Intput:* $ unalias foobar

*Output:* foobar ist nichtmehr ls -la
### Quiz
What command is used to make an alias?

*Answer:* alias

## 19.exit
### Exercise
Exit out of the shell and see what happens. Make sure you don't need to do anymore work in that shell

*1.*

*Intput:* $ exit

*Output:* Verlassen der Shell

### Quiz
How can you exit from the shell?

*Answer:* exit
