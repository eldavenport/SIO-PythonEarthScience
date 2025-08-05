# Creating a Conda Environment

We will use the [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#sharing-an-environment) package manager to manage our Python installation. Conda is great for reproducible science, because it allows you to export your environment configuration in a text file. Another user can then use that text file to create you exact conda environment and run your code.

### Conda commands

`conda create --name <env_name>  # create a new conda environment named env_name`  
`conda create --name <env_name> python=3.12 # create a new conda environment named env_name with a specific Python version`  
`conda activate <env_name>  # activate env_name`  
`conda install <package_name>  # install a package from your default channel, if you installed with miniforge this is the conda-forge channel`  
`conda install -c conda-forge <package_name>  # install a package from the conda-forge channel`  
`conda deactivate  # deactivate the current environment`  

### Creating a new environment from scratch

We will create an environment for use in the Workshop.

`conda create --name sio_software`

Once this is complete, we will activate our environment so that we can install some necessary packages. We will not need to install Python, that is automatically done in the creation of the environment.

`conda activate sio_software`

Now we can install a list of packages for use in the Intro to Python Programming and Plotting session. If you installed conda with miniforge, then you do not need to include `-c conda-forge`.

`conda install -c conda-forge numpy matplotlib jupyterlab netcdf4 pandas`

This command will search for the requested packages and their compatible versions, it will then ask you if you want to proceed with the installation. Continue by entering `y`. After installation we can see the installed packages with:

`conda list` 

To leave your sio_software environment enter:

`conda deactivate`

You may only ever need one conda environment, but you may find over time that you don't want to have every possible package installed in the same place. Perhaps you have some research that needs packages A, B, and C and another project that requires packages X, Y, and Z. In that case you could have to environments, which you can activate for the appropriate use cases. When you make a research or software project public, it is common to release an environment.yml file the can be used to set up a conda environment with the necessary packages.

### Creating a new environment from an environment.yml file

If you have an environment.yml file, you can use it to create a conda environment with the following command:

`conda env create -f environment.yml`

The first line of the .yml file defines the name of the environment. 

### Exporing your environment to a yml file

To export your currently active environment to a yaml file, use the following command:

`conda export > environment.yaml`

To export a specific (not necessarily active) environment to a yaml file, use:

`conda export --name <env_name> --file=environment.yaml`

If we wanted to share our sio_software environment we would use:

`conda export --name sio_software --file=environment.yaml`

There are other formats for sharing, not just YAML. That being said, YAML is cross-platform and is almost always preferred.
