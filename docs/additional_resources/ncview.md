# View NetCDF Files Using ncview

Another useful tool for visualizing NetCDF files is ncview.  Ncview allows 
quick and easy, push-button visualizations of data within NetCDF files.
You can view your data in simple movies, along various dimensions, with different color maps, etc... 

## Installation instructions

There are two different ways you can install ncview on your computer.  The first way is to install ncview in a conda environment.  The second is to install the tool on your computer using Homebrew or from the source code directly.  For the workshop, we recommend installing ncview using conda within a conda environment.  Other installation options are also provided below. 

### Conda

Open a terminal and either activate an existing conda environment or create a new conda environment to install ncview in.  

 1) Ensure you have the correct dependencies. 

    a) Type `conda config --add channels conda-forge` and hit enter. 

    b) Type `conda config --set channel_priority strict` and hit enter. 

 2) Type `conda install ncview` and hit enter. 

### Installation on MacOS 

 1) Open the terminal, type `brew install ncview` and hit enter.

### Installation on Windows

For windows, you need to download the source code from [here](https://cirrus.ucsd.edu/ncview/).  Then you need to configure the source code, using the following steps: 

 1) Extract the archive: tar xvf ncview-*.tar.gz. 
 2) Change directory: cd ncview-*. 
 3) Configure the build: ./configure --with-udunits2_incdir=/path/to/udunits/include --with-udunits2_libdir=/path/to/udunits/lib --prefix=/path/to/install. 
 4) Compile and install: make && make install. 
 5) Add the installation path to your PATH environment variable. 

### Installation on Linux

Open the terminal. 

 1) Terminal command option
 
    b) Type `sudo apt-get install ncview` and hit enter.

 2) Homebrew option

    a) Type `brew install ncview` and hit enter.