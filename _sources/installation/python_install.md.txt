# Python Installation with Conda

Conda is a tool that manages Python packages. You may want to install packages to help you do many different things (plotting, math, interacting with the cloud). Conda will make sure that those packages are compatible with each other and will allow you to set up multiple Python environments that contain the packages you need for each of your projects. 

Download the appropriate version of Miniforge (the conda installer) from [this website](https://conda-forge.org/download/). 

### MacOS 

    1) Download the miniforge version for Apple (either Apple Silicon or Intel depending on which kind of Mac you have)

    2) Open your unix-shell, type `cd ~/Downloads`, and Enter

    3) Type `./Miniforge3-`, hit Tab (this will autocomplete the name of the downloaded file), and Enter

        a) For example, my downloaded filename is: Miniforge3-MacOSX-arm64.sh

    4) Follow the text prompts in the terminal:
        
        a) Press space to move/scroll through the text
        
        b) Type `yes` and Enter to approve the license
        
        c) Hit Enter to approve the default location for installation 

        d) Type `yes` and Enter to add Miniforge to your `PATH`

### WSL and Linux

    1) Download the miniforge version for Linux (x86_64)

    2) Open your unix shell

        a) for WSL users: type `cd /mnt/c/Users/<username>/Downloads` (replace username with your username), and Enter

        b) for Linux users: type `cd ~/Downloads` and Enter

    3) Type `./Miniforge3-`, hit Tab (this will autocomplete the name of the downloaded file), and Enter

        a) For example, your downloaded filename might be: Miniforge3-Linux-x86_64.sh

    4) Follow the text prompts in the terminal:
        
        a) Press space to move/scroll through the text
        
        b) Type `yes` and Enter to approve the license
        
        c) Hit Enter to approve the default location for installation 

        d) Type `yes` and Enter to add Miniforge to your `PATH`

### **All Users**

Close and reopen your unix shell. If conda was installed correctly, you should now see `(base)` before your username, indicating that you are in your base conda environment.

### If you are not Using WSL (i.e. Windows users who can't use WSL)

    1) Download the windows installer from the Miniforge website and run the installer

    2) Follow all of the default options in the installer _except_ you _DO_ need to select “add Miniforge3 to my PATH environment variable”

    3) Open your start menu
    
    4) Search for and run Miniforge Prompt to open a miniforge window where you can use Conda. This is where you will interact with Conda in the future.
