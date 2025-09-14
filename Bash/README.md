#pwd                  present workinf directory
#ls                   lists all files and folders in current directory
#cd [dirname]         changes directory   {if there is a space in the folder name then users like [Name\ 1]}
#cd ..                go back once
#cd ../..             go back twice
#cd ~  or /           changes to home directory
#mkdir [folder name]  make a directoryname [folder name]
#rm file.txt          delete file.txt
#rmdir folder         deltes an emoty folder
#mv oldname.txt       rename
    newname.txt
#ls -l                for show directory with details
#ls -al               for to show hidden directory too with details
#touch file.txt       make a file
#cat [file]           reads the file
#nano vim etc [file]  writes or edits the file
#chmod u+x filename   gives user permission to execute  {if g is used in place or u then permisiion goes to group else user}
#chmod u+w filename   gives user permision to writes    {for r instad of w it gives read permisiion}

#chmod ugo filename   give comand for ugo replaced with num like   ugo is user group and others
                      4 for r 2 for w and 1 for x {add for 2 or more}

#command > filename   cpy paste all the command output  to the filname after formating it #Output redirection operator
#command >> filename  copy paste all the command output and append it #
##we can alsso use avoube one like to add two files in one new like cat a.txt b.txt > c.txt

#man [command]         gives manuall for a command
#head [filename]       prints first 10 lines
#head -n x [filename]  prints first x lines
#tail [filename]       prints lasst 10 lines
#tail -n x [filename]  prints last x lines

#ps                    Info abt current working services
#grep 'str' filename   Searchs for str in file
#grep -v 'str' filename Search for all line which dont have str
#command1|comand2      Outputof 1st became input for second .This is pipe command

**alias** **name**=**'command'** # now you can use name as a vairable for ussing the command 		   anywhere below in the script.
