# Git Cheat Sheet

Common git commands.

| Command | Description |
| :------ | ----------: | 
| git config --global user.name | Set Git username for all directories |
| git config --global user.name | Set Git user email for all directories |
| git init | Initialize a directory as a repository |
| git status | See status of current changed, staged and committed files |
| git add <filename> | Add a file to the staging area to be committed |
| git add <folder> | Add all files in a folder to the staging area |
| git commit -m "<message>" | Commit staged files with a commit message |
| git log | See Git history (commit log) |
| git push | Push any new commits to GitHub |
| git fetch | Fetch information about the remote, without pulling new code down |
| git pull | Pull any new commits from GitHub |
| git merge <from branch> <into branch> | Merge code from one branch into another branch |
| git branch | See list of branches and which you are on |
| git checkout <branch name> | Checkout an existing branch |
| git checkout -b <new branch name> | Checkout a new branch |
| git checkout <commit hash> | Checkout a particular committed vesrion of the code |
| git checkout <filename> | Restore file to latest committed version on current branch |
| git checkout <commit hash> -- <path to file> | Checkout a particular committed version of a single file |
| git show <commit hash>:<path to file> | See a particular committed version of a single file, without changing the file |
| git --set-upstream origin <branch name> | Set a new branch to track itself at origin (first push on new branch) |
| git revert <commit hash> | Undo a particular commit |
| git cherry-pick <commit hash> | Add a single commit |





