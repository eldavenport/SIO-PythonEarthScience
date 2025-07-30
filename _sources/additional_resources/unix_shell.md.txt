# Unix Shell Cheat Sheet

Common commands we will use throughout the workshop (and are generally good for efficiently navigating the unix shell). Wherever you see brackets (\<\>) you should in the appropriate name (i.e., foldername or username).

## Unix Shell Basics

| Command | Description |
| :------ | ----------: | 
| cd \<folderName\> | Enter directory |
| cd .. | Go back one directory |
| cd ∼ |Go to home directory |
| ls | List files within current directory |
| ls \<path to folder\> | List files within another directory |
| pwd | Get directory path |
| clear | Clear terminal |
| mkdir \<foldername\> | Create new folder |
| mv \<path to file\> \<new filename\>| Rename file |
| mv \<path to file\> \<path to new (existing) location\> | Move file to new location |
| mv -r \<path to folder\> \<new foldername\>| Rename folder |
| mv -r \<path to folder\> \<path to new (existing) location\> | Move folder and contents to new location |
| cp \<path to file\> \<path to new (existing) location\> | Copy file to new location |
| cp -r \<path to folder\> \<path to new (existing) location\> | Copy folder and contents to new location |
| rm \<filename\> | Remove file |
| rm -r \<foldername\> | Remove entire folder |
| cat \<filename\> | Print contents of file to terminal |
| head \<filename\> | Print first 10 lines of file |
| echo "Text" | Print text |
| grep "\<PATTERN\>" \<location\> | Find lines matching PATTERN in location |
| help | Get list of commands |
| help name | Get info on command name |

## Additional Unix Shell Commands

| Command | Description | 
| :------ | ----------: | 
| scp \<username\>@\<server address\>:\<file to copy\> \<location to copy to\> | Copy file from remote to local computer |
| scp \<file to copy\> \<username\>@\<server address\>:\<location to copy to\> | Copy file to remote from local computer |
| scp -r \<file to copy\> \<username\>@\<server address\>:\<location to copy to\> | Do the above for a folder and its contents |
| chmod +x \<filename\> | Add execute permissions |
| bash \<script.sh\> | Run a shell script |
| ./\<script.sh\> | Run an executable file |

## vim Editor

| Command | Description |
| :------ | ----------: | 
| vim \<filename\> | create or open a file |
| :w | Save new text |
| :q | Quit file editor |
| :wq | Save and quit file editor in one command |
| :h | Help |
| :split \<path to file\> | Open a second file in split screen |
| i | Begin editing file |
| x | Cut a letter |
| r | Replace a letter |
| yy | Yank (copy) current line |
| dd | Cut and copy current line |
| p | Paste |
| esc | Exit editing mode |

## tmux and screen (Managing Terminal Sessions)

| Command | Description |
| :------ | ----------: | 
| screen -RD | open a screen session or return to existing |
| tmux | create and enter into new file |



