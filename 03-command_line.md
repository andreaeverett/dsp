# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

> >
ls : Lists the contents of a directory.  
ls -a : Lists all files and subdirectories, even if their names begin with a dot (.).  
ls -l : Lists the contents of the directory in long format. This includes information about the file mode, size, owner, group, and last modification date and time.  
ls -lh :  The addition of the ‘h’ modifies the long format to refer to the size of each item using unit suffixes for B, K, M, etc.  
ls -lah : This combines the results of -lh and -a. Items beginning with a dot are included, the long format information is provided, and file sizes are listed with unit suffixes.  
ls -t : This sorts the listed directory items by time modified (with the most recently modified listed first).  
ls -Glp : Again the contents are provided in long format. The -G color codes the items according to their format. In my terminal, directories are blue and text files are black. The -p part adds an additional slash (/) after the name of each subdirectory.  

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > xargs allows you to process a list of arguments by running a command repeatedly on each element in the list.
A simple example is:  
find . -name '*.txt' | xargs grep 'Hello world'  
This tells the shell to find all .txt files in the current directory and for each one that contains the text 'Hello world,' to print the filename along with any lines that contain that string.

 

