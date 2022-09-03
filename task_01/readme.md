<h2> Within this file I will be including my answers to the questions posed in the challenge as well as the documentation I create for commands I run.</h2>

The linux operating system makes no differentiation between files and directories. In fact, everything is either a file or a process.

For example, a file might be this markdown file. A process might be something that opens this file and reads or writes to it.



<h3>Can you explain how “Links” increments and decrements for directories and files?</h3>

Links increments per file. See the result of stat ```stat nested01/``` which contains 3 links to /nested_file01 , /nested_02/, and a link to its parent "..". 

The "symbolic" directory is a link that functions like a shortcut in windows. It's just a pointer to nested_01/ and created with ```ln -s nested_01/ symbolic```
Observe how ```stat symbolic``` returns one Links: 1 because it does not follow the shortcut. You may follow the shortcut link with ```stat -s /sym_link/``` which returns Links: 3 just like ```stat nested_01/```.

<h3>What command can you use to target a file via inode number?</h3>

```find -inum 52692408``` returns ./nested_01. ```find``` is the standard way to find a file in ubuntu and -inum searches by inode number.

<h3>What are the Links in an empty directory?</h3>

The hidden links "." and ".." are links to the current directory and the parent directory respectively. These are the two links referred to in ```stat empty/```. You can view them with ```ls -a```.

 <h3>How do stat links relate to the ln function?</h3> 

 The symbolic link I created links like a shortcut to nested_01/. You can also create a "hard link". A hard link is another name for a file and cannot be created for a directory. I've created a hard link "stat_hard_link" for the "stat.txt" file. Also, you can see that both the hard link and the original file name share the same inode number.
 
  In contrast, a soft link can be used for a directory and I've made one called symbolic. It does not share the same inode as the original directory and won't even display an intuitive number of links if you use ```stat``` on it without using the ```-L``` argument to follow the link first.


<h3>While investigating this system, what were the most useful/informative commands?</h3>

```man stat | col -b > stat.txt``` to dump to linux manual page for ```stat```. The man page is the best way to learn any command.

<h3>Document all your discoveries, experiments including commands and their results in a markdown document or text file and submit to a public github account. We are interested in how deeply you investigate, how organized and thorough your notes are.</h3>
