# Windows Instructions for Unix Shell 

These instructions will walk you through the installation of Windows Subsystem for Linux (WSL). WSL allows you to run Linux on your Windows computer. This will allow you to create files, run software, and navigate your filesystem as if you were on a Linux computer. Your work will still be available to you through the Windows interface as well. Most modern software tools are designed to be used on Unix systems like Linux or MacOS. 

If you cannot install WSL because your Windows version is too old, then you should use Git Bash (instructions included).

### **Windows Subsystem for Linux (WSL)**

Linux is the industry standard operating system for most servers including super computers. This will allow you to use the same workflow interchangeably between your laptop and any remote servers. Installing Git is trivial once you have WSL.

    1) Open the windows start menu and search “store” to open the Microsoft Store.

    2) In the store search “wsl ubuntu”. (Ubuntu is the version of Linux you are installing)

    3) Select ‘Ubuntu 24.04.01-LTS’ if it is available. If not select ‘Ubuntu 22.04.1-LTS’

    4) If a terminal window pops up asking to continue, press space to continue.

    5) If a new pop-up window appears asking to make changes to your device, say “yes”.

    6) Once installation is complete, restart your computer.

    7) Once restarted go to the windows start menu and type “Ubuntu” to run the installed Linux operating system. 
        
        a) This will open a unix-shell with bash and you will do this any time you want to use WSL.

    8) Type `sudo apt update` and Enter 

        a) apt is a command that will manage updating/installing things in Linux. Any time you use sudo you will need to enter your password.

    9) Type `sudo apt install autotools python3` and Enter 

### To access Windows system files from Linux

Navigate to `/mnt/c` in the WSL terminal by typing `cd /mnt/c`. Now when you type `ls` and Enter, you should see all of the files and folders that already exist on your Windows computer.

### To access Linux subsystem files from Windows 

    1) in Powershell, navigate to `\\wsl.localhost\`

    2) in File Explorer, click the Linux Icon (it's a penguin) in the File Explorer bar 

### **Git Bash from Git For Windows**

Download Git for Windows [here](https://gitforwindows.org/).


This will come with an application called Git Bash that allows you to use Git commands in a terminal-like environment. The issue is that this does not support other Unix-shell commands so you will be limited compared to using WSL. Detailed instructions for installation are below to get both bash and Git to work properly. If you go this route, then you do not need a separate installation of Git (you can skip the Git installation instructions.)

    Run the installer and follow the steps below:

    1) Click on "Next" four times (two times if you've previously installed Git). You don't need to change anything in the Information, location, components, and start menu screens.

    2) From the dropdown menu, "Choosing the default editor used by Git", select "Use the Nano editor by default" (NOTE: you will need to scroll up to find it) and click on "Next".

    3) On the page that says "Adjusting the name of the initial branch in new repositories", ensure that "Let Git decide" is selected. 

    4) Ensure that "Git from the command line and also from 3rd-party software" is selected and click on "Next". 
        
        a) If you don't do this Git Bash will not work properly, requiring you to remove the Git Bash installation, re-run the installer and to select the "Git from the command line and also from 3rd-party software" option.

    5) Select "Use bundled OpenSSH".


    6) Ensure that "Use the native Windows Secure Channel Library" is selected and click on "Next".

    7) Ensure that "Checkout Windows-style, commit Unix-style line endings" is selected and click on "Next".

    8) Ensure that "Use Windows' default console window" is selected and click on "Next".

    9) Ensure that "Default (fast-forward or merge) is selected and click "Next"

    10) Ensure that "Git Credential Manager" is selected and click on "Next".

    11) Ensure that "Enable file system caching" is selected and click on "Next".

    12) Click on "Install".

    13) Click on "Finish" or "Next".

    14) If your "HOME" environment variable is not set (or you don't know what this is):
        
        a) Open command prompt (Open Start Menu then type `cmd` and press Enter)
        
        b) Type the following line into the command prompt window exactly as shown: `setx HOME "%USERPROFILE%"`

        c) Press Enter, you should see SUCCESS: Specified value was saved.
        
        d) Quit command prompt by typing exit then pressing Enter

Git Bash installation instructions are from the [Software Carpentries Website](https://carpentries.github.io/workshop-template/install_instructions/#shell).